/*!
 * BrightlyFuture AI Writing Pattern Checker – core (v2)
 * Pure functions, no DOM. Runs in the browser and in Node for testing.
 */
(function (root) {
  'use strict';

  // Words and phrases that appear far more often in unedited LLM output than in
  // human writing. Weight 2 = strong tell, 1 = mild tell.
  var AI_MARKERS = [
    ['delve', 2], ['tapestry', 2], ['testament to', 2], ['in today\'s', 2], ['ever-evolving', 2], ['ever-changing', 2],
    ['rapidly evolving', 2], ['digital landscape', 2], ['landscape', 1], ['realm', 2], ['embark', 2], ['unlock', 1],
    ['unleash', 2], ['harness', 2], ['foster', 2], ['fostering', 2], ['leverage', 2], ['leveraging', 2], ['seamless', 2],
    ['seamlessly', 2], ['robust', 1], ['pivotal', 2], ['crucial', 1], ['vital', 1], ['essential', 1], ['comprehensive', 1],
    ['elevate', 2], ['empower', 2], ['streamline', 2], ['cutting-edge', 2], ['innovative', 1], ['transformative', 2],
    ['game-changer', 2], ['navigate', 1], ['navigating', 1], ['intricate', 2], ['multifaceted', 2], ['nuanced', 1],
    ['plays a crucial role', 2], ['plays a key role', 2], ['plays a vital role', 2], ['it is important to', 2],
    ['it\'s important to', 2], ['it is essential to', 2], ['it is crucial', 2], ['it is worth noting', 2],
    ['additionally', 1], ['furthermore', 2], ['moreover', 2], ['ultimately', 1], ['in conclusion', 2], ['overall,', 1],
    ['whether you are', 2], ['whether you\'re', 2], ['like never before', 2], ['take your', 1], ['to the next level', 2],
    ['a wide range of', 1], ['a variety of', 1], ['numerous', 1], ['various', 1], ['enhance', 1], ['optimal', 1],
    ['ensure', 1], ['ensures', 1], ['ensuring', 1], ['myriad', 2], ['plethora', 2], ['paramount', 2], ['holistic', 2],
    ['synergy', 2], ['in this article', 2], ['we will explore', 2], ['let\'s explore', 2], ['dive into', 2], ['deep dive', 2],
    ['key differentiator', 2], ['customer-centric', 2], ['proactive approach', 2], ['long-term success', 2],
    ['sustainable growth', 2], ['full potential', 2], ['work smarter', 2], ['more than ever', 1], ['alike', 1],
    ['valuable insights', 2], ['actionable', 1], ['stand out', 1], ['significantly', 1], ['profound', 1], ['equitable', 1],
    ['a testament', 2], ['serves as', 1], ['at the forefront', 2], ['shape the future', 2], ['reshaping', 2]
  ];
  var TRANSITION_OPENERS = /^(Additionally|Furthermore|Moreover|However|Ultimately|Overall|In addition|Consequently|Therefore|Thus|Notably|Importantly|In conclusion|By [a-z]+ing|Whether you|With [a-z]+ |From [a-z]+ to|As a result|In today's|Finally|Next|Firstly|Secondly|Lastly)\b/;
  var CONTRACTIONS = /\b(I'm|I've|I'd|I'll|don't|doesn't|didn't|can't|won't|isn't|aren't|wasn't|weren't|it's|that's|there's|you're|we're|they're|you've|we've|couldn't|wouldn't|shouldn't|hadn't|haven't|let's|he's|she's)\b/gi;
  var FIRST_PERSON = /\b(I|me|my|mine|we|our|us)\b/g;
  var HEDGE_GENERIC = /\b(can help|help you|allows you to|enables you to|you can|should|be sure to|make sure|consider|it is recommended)\b/gi;

  // Fitted 27 Sept 2026 on 252 texts (HC3 ChatGPT/human answers + pre-AI human writing).
  var WEIGHTS = {"bias": -0.1777, "hedges": 0.1667, "frames": 0.6438, "informal": -0.5674, "parens": -0.3682, "longWords": -0.1553, "richness": -0.6693, "markers": 0.5294, "triads": 0.282, "openers": 0.0918, "generic": -0.0471, "specificity": 0.1446, "voice": -0.3059, "variation": -0.6336, "avgLen": -0.352};
  var MEANS = {"hedges": 2.028, "frames": 0.4862, "informal": 0.2689, "parens": 0.5813, "longWords": 11.1543, "richness": 5.1935, "markers": 0.4444, "triads": 0.1568, "openers": 0.0278, "generic": 0.3039, "specificity": 3.9819, "voice": 1.0186, "variation": 0.4124, "avgLen": 23.1201};
  var SDS = {"hedges": 1.5166, "frames": 0.666, "informal": 0.7684, "parens": 1.0062, "longWords": 6.1227, "richness": 1.018, "markers": 0.7419, "triads": 0.2547, "openers": 0.0632, "generic": 0.6144, "specificity": 6.1424, "voice": 1.9463, "variation": 0.184, "avgLen": 8.1448};
  function setModel(w, m, sd) { WEIGHTS = w; MEANS = m; SDS = sd; }

  function sentencesOf(text) {
    var s = text.replace(/\s+/g, ' ').match(/[^.!?]+(?:[.!?]+["')\]]*|$)/g) || [];
    return s.map(function (x) { return x.trim(); }).filter(function (x) { return /[A-Za-z]/.test(x); });
  }
  function wordsOf(t) { return t.match(/[A-Za-z0-9'’-]+/g) || []; }
  function clamp(x, a, b) { return Math.max(a, Math.min(b, x)); }

  function markerHits(sentence) {
    var lc = ' ' + sentence.toLowerCase() + ' ';
    var hits = [];
    for (var i = 0; i < AI_MARKERS.length; i++) {
      var m = AI_MARKERS[i][0];
      var re = new RegExp('(^|[^a-z])' + m.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '(?=[^a-z]|$)', 'g');
      var c = (lc.match(re) || []).length;
      if (c) hits.push({ term: m, weight: AI_MARKERS[i][1] * c });
    }
    return hits;
  }

  // Share of sentences that contain an "X, Y, and Z" style list of three.
  function triadCount(sentence) { return (sentence.match(/\b[\w-]+(?: [\w-]+){0,2}, [\w-]+(?: [\w-]+){0,2},? (and|or) [\w-]+/g) || []).length; }

  function specificityCount(sentence, isFirst) {
    var n = 0;
    n += (sentence.match(/\b\d[\d,.:%£$€]*\b/g) || []).length;                  // numbers, prices, times
    n += (sentence.match(/["“][^"”]{3,}["”]/g) || []).length;                    // quotes
    var w = sentence.split(/\s+/);
    for (var i = 1; i < w.length; i++) if (/^[A-Z][a-z]+/.test(w[i]) && !/^(I|I'm|I've|I'd)$/.test(w[i])) n++; // names mid-sentence
    return n;
  }

  function analyse(text) {
    var sents = sentencesOf(text);
    var words = wordsOf(text);
    var W = Math.max(1, words.length), S = Math.max(1, sents.length);
    var lens = sents.map(function (s) { return wordsOf(s).length; });
    var mean = lens.reduce(function (a, b) { return a + b; }, 0) / S;
    var sd = Math.sqrt(lens.reduce(function (a, b) { return a + (b - mean) * (b - mean); }, 0) / S);
    var cv = mean ? sd / mean : 0;

    var markerWeight = 0, triads = 0, openers = 0, spec = 0, perSentence = [];
    sents.forEach(function (s, i) {
      var hits = markerHits(s);
      var mw = hits.reduce(function (a, h) { return a + h.weight; }, 0);
      var tr = triadCount(s);
      var op = TRANSITION_OPENERS.test(s) ? 1 : 0;
      var sp = specificityCount(s, i === 0);
      var fp = (s.match(FIRST_PERSON) || []).length + (s.match(CONTRACTIONS) || []).length;
      var gen = (s.match(HEDGE_GENERIC) || []).length;
      markerWeight += mw; triads += tr; openers += op; spec += sp;
      // Sentence score: evidence for AI style minus evidence for a human voice.
      var raw = 1.1 * mw + 1.2 * tr + 1.3 * op + 0.6 * gen - 0.8 * sp - 0.9 * fp;
      var len = lens[i];
      if (len >= 18 && len <= 30) raw += 0.4;
      if (len <= 7) raw -= 0.7;
      var reasons = [];
      hits.slice(0, 3).forEach(function (h) { reasons.push('"' + h.term + '"'); });
      if (tr) reasons.push('list of three');
      if (op) reasons.push('stock transition opener');
      if (gen) reasons.push('generic advice phrasing');
      perSentence.push({ text: s, raw: raw, reasons: reasons, human: sp + fp > 0 });
    });

    var contractions = (text.match(CONTRACTIONS) || []).length;
    var firstPerson = (text.match(FIRST_PERSON) || []).length;
    var generic = (text.match(HEDGE_GENERIC) || []).length;

    var lower = text.toLowerCase();
    var hedges = (lower.match(/\b(may|might|can|could|generally|typically|often|usually|various|several|certain|potentially|overall|also)\b/g) || []).length;
    var stockFrames = (lower.match(/\b(there are (several|many|a few|a number of)|it is (also|not uncommon|generally|possible|important|essential|likely)|in general|for example|in other words|this means that|this can|this is because|some people|depending on|in addition|as well as|it's (also|important|possible|not uncommon))\b/g) || []).length;
    var informal = (text.match(/\b(lol|gonna|wanna|kinda|u|ur|im|dont|doesnt|cant|thats|yeah|yep|nope|ok|okay|stuff|guy|guys|pretty much|basically|actually|honestly)\b/gi) || []).length
      + (text.match(/(^|[.!?]\s+)[a-z]/g) || []).length + (text.match(/[!?]{2,}|\.\.\.|:\)|\*/g) || []).length;
    var parens = (text.match(/\(/g) || []).length;
    var longWords = words.filter(function (w) { return w.length >= 9; }).length;
    var uniq = {}; words.forEach(function (w) { uniq[w.toLowerCase()] = 1; });
    var ttr = Object.keys(uniq).length / Math.sqrt(2 * W); // Guiraud-style, length-robust
    var f = {
      hedges: 100 * hedges / W,
      frames: 100 * stockFrames / W,
      informal: 100 * informal / W,
      parens: 100 * parens / W,
      longWords: 100 * longWords / W,
      richness: ttr,
      markers: 100 * markerWeight / W,        // weighted AI markers per 100 words
      triads: triads / S,                      // lists of three per sentence
      openers: openers / S,                    // share of sentences with stock openers
      generic: 100 * generic / W,              // generic advice phrases per 100 words
      specificity: 100 * spec / W,             // numbers, names, quotes per 100 words
      voice: 100 * (contractions + firstPerson) / W, // first person + contractions per 100 words
      variation: cv,                           // sentence-length variation (burstiness)
      avgLen: mean
    };

    // Logistic model; weights fitted on a training split of public data (see REVIEW.md).
    var z = WEIGHTS.bias;
    for (var k in WEIGHTS) if (k !== 'bias' && f[k] !== undefined) z += WEIGHTS[k] * (f[k] - MEANS[k]) / SDS[k];
    var score = clamp(Math.round(100 / (1 + Math.exp(-z))), 1, 99);

    perSentence.forEach(function (p) {
      p.level = p.raw >= 2.2 ? 'high' : p.raw >= 1 ? 'some' : 'low';
    });

    return { score: score, features: f, sentences: perSentence, words: W, count: S };
  }

  var api = { analyse: analyse, sentencesOf: sentencesOf, setModel: setModel };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  root.BFDetectorCore = api;
})(typeof window !== 'undefined' ? window : this);
