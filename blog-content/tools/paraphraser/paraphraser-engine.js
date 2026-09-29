/*!
 * BrightlyFuture Paraphraser engine v2
 * Drop-in replacement for the inline script on /ai-paraphrase-rewriter/.
 * AI rewrite via the free Pollinations API; falls back to the in-browser rule engine below.
 */
(function (root) {
  'use strict';

  /* ------------------------------------------------------------------ *
   * 1. Phrase rules (applied first, longest phrases first).
   *    Each entry: [pattern, {mode: [alternatives]}]; "all" = any mode.
   * ------------------------------------------------------------------ */
  var PHRASES = [
    ['in order to', { all: ['to'], formal: ['so as to', 'to'], academic: ['in order to', 'so as to'] }],
    ['a wide variety of', { all: ['many', 'a range of'], simple: ['many'], academic: ['a broad range of'] }],
    ['a large number of', { all: ['many', 'plenty of'], simple: ['many'], formal: ['numerous'] }],
    ['a lot of', { all: ['many', 'plenty of'], formal: ['numerous'], academic: ['numerous'] }],
    ['lots of', { all: ['plenty of', 'many'], formal: ['numerous'] }],
    ['due to the fact that', { all: ['because'], academic: ['because', 'given that'] }],
    ['because of the fact that', { all: ['because'] }],
    ['in spite of the fact that', { all: ['although'] }],
    ['despite the fact that', { all: ['although', 'even though'] }],
    ['at this point in time', { all: ['now', 'at present'], simple: ['now'] }],
    ['at the present time', { all: ['now', 'currently'], simple: ['now'] }],
    ['in the event that', { all: ['if'], formal: ['should', 'if'] }],
    ['with regard to', { all: ['about', 'on'], formal: ['regarding', 'concerning'] }],
    ['with respect to', { all: ['about', 'regarding'], simple: ['about'] }],
    ['in relation to', { all: ['about', 'regarding'], simple: ['about'] }],
    ['is able to', { all: ['can'], formal: ['is able to', 'can'] }],
    ['are able to', { all: ['can'] }],
    ['was able to', { all: ['managed to'] }],
    ['were able to', { all: ['managed to'] }],
    ['has the ability to', { all: ['can'] }],
    ['have the ability to', { all: ['can'] }],
    ['it is important to', { all: ['you should', 'make sure to'], formal: ['it is essential to'], academic: ['it is essential to'] }],
    ['it is essential that', { all: ['you must make sure that'], formal: ['it is vital that'] }],
    ['make sure to', { all: ['be sure to', 'remember to'], formal: ['be sure to'] }],
    ['need to', { all: ['have to', 'must'], casual: ['need to', 'have to'], simple: ['have to'] }],
    ['needs to', { all: ['has to', 'must'], simple: ['has to'] }],
    ['depend on', { all: ['rely on'], formal: ['rely upon', 'rely on'] }],
    ['depends on', { all: ['relies on', 'hinges on'], simple: ['relies on'] }],
    ['without warning', { all: ['with no notice', 'without notice'] }],
    ['make sure', { all: ['ensure', 'check'], casual: ['make sure'], simple: ['check'] }],
    ['find out', { all: ['learn', 'discover'], casual: ['find out'], formal: ['determine', 'establish'] }],
    ['figure out', { all: ['work out', 'determine'], formal: ['determine'], simple: ['work out'] }],
    ['look at', { all: ['examine', 'review', 'check'], casual: ['check out'], simple: ['check'] }],
    ['look for', { all: ['search for', 'seek'], simple: ['search for'] }],
    ['come up with', { all: ['create', 'develop'], simple: ['make'], formal: ['devise'] }],
    ['get rid of', { all: ['remove', 'eliminate'], simple: ['remove'] }],
    ['make changes', { all: ['change things', 'make updates'], formal: ['implement changes'], simple: ['change things'] }],
    ['set up', { all: ['create', 'build'], simple: ['make'], formal: ['establish'] }],
    ['put together', { all: ['assemble', 'build'], simple: ['build'] }],
    ['carry out', { all: ['perform', 'complete'], simple: ['do'], formal: ['conduct'] }],
    ['point out', { all: ['note', 'highlight'], simple: ['show'] }],
    ['take into account', { all: ['consider', 'allow for'], simple: ['think about'] }],
    ['on the other hand', { all: ['however', 'by contrast'], simple: ['but'], casual: ['then again'] }],
    ['as a result', { all: ['so', 'because of this'], formal: ['consequently', 'as a consequence'], academic: ['consequently'] }],
    ['for example', { all: ['for instance', 'such as'], simple: ['for example'] }],
    ['for instance', { all: ['for example'] }],
    ['such as', { all: ['like'], formal: ['such as'], academic: ['such as'] }],
    ['in addition to', { all: ['as well as', 'besides'] }],
    ['as well as', { all: ['and', 'along with'] }],
    ['a number of', { all: ['several', 'some'] }],
    ['the majority of', { all: ['most'], academic: ['most', 'the bulk of'] }],
    ['in most cases', { all: ['usually', 'mostly'], formal: ['generally'] }],
    ['first of all', { all: ['first', 'to start'] }],
    ['in conclusion', { all: ['to sum up', 'overall'], simple: ['in short'] }],
    ['each and every', { all: ['every'] }],
    ['already seen', { all: ['seen before', 'already read'] }],
    ['works best', { all: ['works best', 'performs best', 'is most effective'], simple: ['works best'] }],
    ['first-hand', { all: ['first-hand', 'direct', 'your own'] }]
  ];

  /* ------------------------------------------------------------------ *
   * 2. Word rules. Keys are base forms. Alternatives are chosen so that
   *    each mode moves text in its own direction (Simple never makes
   *    a word longer; Formal/Academic never make it more casual).
   *    POS: v = verb, a = adjective/adverb, n = noun.
   *    Ambiguous verbs (also common nouns) are flagged amb:true and only
   *    replaced when the word before them marks a verb.
   * ------------------------------------------------------------------ */
  var WORDS = {
    // verbs
    use: { p: 'v', all: ['apply', 'rely on'], simple: [], formal: ['employ'], academic: ['employ', 'utilise'], amb: true },
    utilise: { p: 'v', all: ['use'], simple: ['use'], formal: ['employ'], academic: ['employ'] },
    utilize: { p: 'v', all: ['use'], simple: ['use'], formal: ['employ'] },
    help: { p: 'v', all: ['assist', 'support'], simple: [], casual: ['help'], formal: ['assist', 'support'], amb: true, noTo: true },
    assist: { p: 'v', all: ['help', 'support'], simple: ['help'] },
    show: { p: 'v', all: ['reveal', 'highlight'], simple: [], formal: ['demonstrate', 'indicate'], academic: ['demonstrate', 'indicate'], amb: true },
    demonstrate: { p: 'v', all: ['show', 'prove'], simple: ['show'] },
    check: { p: 'v', all: ['review', 'examine', 'see'], simple: ['see'], formal: ['review', 'examine'], amb: true },
    note: { p: 'v', all: ['record', 'write down'], simple: ['write down'], formal: ['record', 'observe'], amb: true },
    add: { p: 'v', all: ['include', 'bring in'], simple: [], formal: ['include', 'incorporate'] },
    get: { p: 'v', all: ['gain', 'earn'], simple: [], casual: ['get'], formal: ['obtain', 'achieve'], academic: ['obtain'] },
    obtain: { p: 'v', all: ['get', 'gain'], simple: ['get'] },
    give: { p: 'v', all: ['offer', 'provide'], simple: [], formal: ['provide'] },
    provide: { p: 'v', all: ['offer', 'give'], simple: ['give'] },
    create: { p: 'v', all: ['make', 'build'], simple: ['make'], formal: ['develop', 'produce'] },
    build: { p: 'v', all: ['create', 'develop'], simple: ['make'] },
    start: { p: 'v', all: ['begin', 'launch'], simple: [], formal: ['begin', 'commence'], amb: true },
    begin: { p: 'v', all: ['start'], simple: ['start'] },
    commence: { p: 'v', all: ['begin', 'start'], simple: ['start'] },
    end: { p: 'v', all: ['finish', 'close'], simple: [], formal: ['conclude'], amb: true },
    finish: { p: 'v', all: ['complete', 'wrap up'], simple: ['end'], formal: ['complete'] },
    try: { p: 'v', all: ['attempt', 'test'], simple: [], formal: ['attempt'], amb: true },
    attempt: { p: 'v', all: ['try'], simple: ['try'] },
    think: { p: 'v', all: ['believe', 'consider'], simple: [], formal: ['consider', 'believe'] },
    consider: { p: 'v', all: ['think about', 'weigh up'], simple: ['think about'], formal: ['evaluate'] },
    need: { p: 'v', all: ['require'], simple: [], casual: ['need'], formal: ['require'], amb: true, noTo: true },
    require: { p: 'v', all: ['need'], simple: ['need'] },
    want: { p: 'v', all: ['would like', 'hope'], simple: [], formal: ['wish', 'intend'] },
    keep: { p: 'v', all: ['maintain', 'hold on to'], simple: [], formal: ['maintain', 'retain'] },
    maintain: { p: 'v', all: ['keep'], simple: ['keep'] },
    change: { p: 'v', all: ['adjust', 'alter'], simple: [], formal: ['modify', 'alter'], amb: true },
    modify: { p: 'v', all: ['change', 'adjust'], simple: ['change'] },
    find: { p: 'v', all: ['discover', 'identify'], simple: [], formal: ['identify', 'locate'] },
    identify: { p: 'v', all: ['spot', 'find'], simple: ['find'] },
    tell: { p: 'v', all: ['inform', 'let know'], simple: [], formal: ['inform', 'advise'] },
    buy: { p: 'v', all: ['purchase'], simple: [], formal: ['purchase', 'acquire'] },
    purchase: { p: 'v', all: ['buy'], simple: ['buy'] },
    improve: { p: 'v', all: ['strengthen', 'upgrade'], simple: ['fix'], formal: ['enhance', 'strengthen'] },
    increase: { p: 'v', all: ['raise', 'boost'], simple: ['raise'], formal: ['raise', 'expand'], amb: true },
    reduce: { p: 'v', all: ['cut', 'lower'], simple: ['cut'], formal: ['decrease', 'lower'] },
    explain: { p: 'v', all: ['describe', 'clarify'], simple: ['describe'], formal: ['clarify', 'set out'] },
    answer: { p: 'v', all: ['address', 'respond to'], simple: [], formal: ['address', 'respond to'], amb: true },
    repeat: { p: 'v', all: ['echo', 'rehash'], simple: [], formal: ['reiterate', 'duplicate'] },
    publish: { p: 'v', all: ['release', 'put out'], simple: ['put out'], formal: ['release', 'issue'] },
    write: { p: 'v', all: ['draft'], simple: [], formal: ['compose', 'draft'] },
    rank: { p: 'v', all: ['appear', 'show up'], simple: ['show up'], formal: ['appear', 'feature'], amb: true },
    include: { p: 'v', all: ['cover', 'contain'], simple: ['cover'] },
    choose: { p: 'v', all: ['pick', 'select'], simple: ['pick'], formal: ['select'] },
    select: { p: 'v', all: ['choose', 'pick'], simple: ['pick'] },
    allow: { p: 'v', all: ['enable'], simple: [], formal: ['enable', 'permit'] },
    understand: { p: 'v', all: ['grasp', 'follow'], simple: ['get'], formal: ['comprehend', 'grasp'] },
    focus: { p: 'v', all: ['concentrate'], simple: [], formal: ['concentrate'], amb: true },
    avoid: { p: 'v', all: ['skip', 'steer clear of'], simple: ['skip'], formal: ['prevent', 'refrain from'] },
    discuss: { p: 'v', all: ['cover', 'talk about'], simple: ['talk about'], formal: ['examine', 'address'] },
    // adjectives / adverbs
    clear: { p: 'a', all: ['simple', 'focused'], simple: [], formal: ['precise', 'well-defined'] },
    specific: { p: 'a', all: ['particular'], simple: [], formal: ['particular', 'defined'] },
    important: { p: 'a', all: ['key', 'vital'], simple: ['key'], formal: ['significant', 'essential'], academic: ['significant'] },
    significant: { p: 'a', all: ['important', 'major'], simple: ['big'] },
    big: { p: 'a', all: ['large', 'major'], simple: [], formal: ['substantial', 'considerable'] },
    large: { p: 'a', all: ['big', 'sizeable'], simple: ['big'], formal: ['substantial'] },
    good: { p: 'a', all: ['strong', 'solid'], simple: [], formal: ['effective', 'sound'] },
    bad: { p: 'a', all: ['weak', 'poor'], simple: [], formal: ['poor', 'ineffective'] },
    easy: { p: 'a', all: ['simple', 'straightforward'], simple: ['simple'], formal: ['straightforward'] },
    hard: { p: 'a', all: ['difficult', 'tough'], simple: ['tough'], formal: ['difficult', 'challenging'] },
    difficult: { p: 'a', all: ['hard', 'tough'], simple: ['hard'] },
    fast: { p: 'a', all: ['quick', 'rapid'], simple: ['quick'], formal: ['rapid', 'swift'] },
    quick: { p: 'a', all: ['fast', 'rapid'], simple: ['fast'] },
    new: { p: 'a', all: ['fresh', 'recent'], simple: [], formal: ['recent', 'novel'] },
    main: { p: 'a', all: ['key', 'core', 'central'], simple: ['key'], formal: ['principal', 'primary'] },
    whole: { p: 'a', all: ['entire', 'full'], simple: ['full'] },
    entire: { p: 'a', all: ['whole', 'full'], simple: ['whole'] },
    many: { p: 'a', all: ['numerous', 'plenty of'], simple: [], casual: ['lots of'], formal: ['numerous'] },
    often: { p: 'a', all: ['frequently', 'regularly'], simple: [], formal: ['frequently'] },
    usually: { p: 'a', all: ['typically', 'normally'], simple: [], formal: ['typically', 'generally'] },
    really: { p: 'a', all: ['truly', 'genuinely'], simple: [], casual: ['really'], formal: ['genuinely'] },
    very: { p: 'a', all: ['highly', 'extremely'], simple: [], casual: ['really'], formal: ['highly'] },
    also: { p: 'a', all: ['too', 'as well'], simple: [], formal: ['also', 'in addition'] },
    however: { p: 'a', all: ['but', 'still'], simple: ['but'], formal: ['however', 'nevertheless'] },
    enough: { p: 'a', all: ['sufficient'], simple: [], formal: ['sufficient', 'adequate'] },
    sufficient: { p: 'a', all: ['enough'], simple: ['enough'] },
    approximately: { p: 'a', all: ['about', 'roughly', 'around'], simple: ['about'] },
    about: { p: 'a', all: [], formal: ['approximately'], academic: ['approximately'] },
    already: { p: 'a', all: [], simple: [] },
    // nouns (safe, low ambiguity)
    article: { p: 'n', all: ['post', 'piece'], simple: ['post'], formal: ['article', 'piece'] },
    post: { p: 'n', all: ['article', 'piece'], simple: [], formal: ['article'], amb: true },
    reader: { p: 'n', all: ['visitor', 'reader'], simple: [], formal: ['reader'] },
    question: { p: 'n', all: ['query', 'problem'], simple: [], formal: ['query'], amb: true },
    problem: { p: 'n', all: ['issue', 'challenge'], simple: ['issue'], formal: ['issue', 'challenge'] },
    issue: { p: 'n', all: ['problem', 'concern'], simple: ['problem'] },
    idea: { p: 'n', all: ['concept', 'thought'], simple: [], formal: ['concept', 'notion'] },
    method: { p: 'n', all: ['approach', 'technique'], simple: ['way'], formal: ['approach', 'technique'] },
    way: { p: 'n', all: ['method', 'approach'], simple: [], formal: ['method', 'means'] },
    result: { p: 'n', all: ['outcome'], simple: [], formal: ['outcome'], amb: true },
    goal: { p: 'n', all: ['aim', 'target'], simple: ['aim'], formal: ['objective', 'aim'] },
    benefit: { p: 'n', all: ['advantage', 'gain'], simple: ['gain'], formal: ['advantage'], amb: true },
    tool: { p: 'n', all: ['utility', 'resource'], simple: [], formal: ['resource', 'utility'] },
    data: { p: 'n', all: ['figures', 'evidence'], simple: ['figures'], formal: ['evidence', 'data'] },
    angle: { p: 'n', all: ['approach', 'perspective'], simple: ['approach'], formal: ['perspective'] },
    customer: { p: 'n', all: ['client', 'buyer'], simple: ['buyer'], formal: ['client'] },
    business: { p: 'n', all: ['company', 'firm'], simple: ['company'], formal: ['organisation', 'company'] },
    company: { p: 'n', all: ['business', 'firm'], simple: ['business'], formal: ['organisation'] },
    effective: { p: 'a', all: ['useful', 'powerful', 'reliable'], simple: ['useful'], formal: ['effective', 'productive'] },
    relationship: { p: 'n', all: ['connection', 'bond'], simple: ['link'], formal: ['relationship', 'connection'] },
    drop: { p: 'v', all: ['fall', 'decline'], simple: ['fall'], formal: ['decline', 'decrease'], amb: true },
    fall: { p: 'v', all: ['drop', 'decline'], simple: ['drop'] },
    client: { p: 'n', all: ['customer'], simple: ['customer'] },
    team: { p: 'n', all: ['team'], simple: [] },
    website: { p: 'n', all: ['site'], simple: ['site'], formal: ['website'] },
    rankings: { p: 'n', all: ['positions', 'rankings'], simple: [] },
    channel: { p: 'n', all: ['platform', 'route'], simple: [], formal: ['channel', 'medium'] },
    people: { p: 'n', all: ['readers', 'users'], simple: [], formal: ['individuals', 'users'] }
  };

  var IRREGULAR = {
    get: { s: 'gets', ed: 'got', ing: 'getting', en: 'got' },
    give: { s: 'gives', ed: 'gave', ing: 'giving', en: 'given' },
    make: { s: 'makes', ed: 'made', ing: 'making', en: 'made' },
    build: { s: 'builds', ed: 'built', ing: 'building', en: 'built' },
    begin: { s: 'begins', ed: 'began', ing: 'beginning', en: 'begun' },
    think: { s: 'thinks', ed: 'thought', ing: 'thinking', en: 'thought' },
    keep: { s: 'keeps', ed: 'kept', ing: 'keeping', en: 'kept' },
    find: { s: 'finds', ed: 'found', ing: 'finding', en: 'found' },
    tell: { s: 'tells', ed: 'told', ing: 'telling', en: 'told' },
    buy: { s: 'buys', ed: 'bought', ing: 'buying', en: 'bought' },
    write: { s: 'writes', ed: 'wrote', ing: 'writing', en: 'written' },
    choose: { s: 'chooses', ed: 'chose', ing: 'choosing', en: 'chosen' },
    understand: { s: 'understands', ed: 'understood', ing: 'understanding', en: 'understood' },
    show: { s: 'shows', ed: 'showed', ing: 'showing', en: 'shown' },
    hold: { s: 'holds', ed: 'held', ing: 'holding', en: 'held' },
    run: { s: 'runs', ed: 'ran', ing: 'running', en: 'run' },
    put: { s: 'puts', ed: 'put', ing: 'putting', en: 'put' },
    set: { s: 'sets', ed: 'set', ing: 'setting', en: 'set' },
    grasp: { s: 'grasps', ed: 'grasped', ing: 'grasping', en: 'grasped' },
    let: { s: 'lets', ed: 'let', ing: 'letting', en: 'let' },
    seek: { s: 'seeks', ed: 'sought', ing: 'seeking', en: 'sought' },
    spot: { s: 'spots', ed: 'spotted', ing: 'spotting', en: 'spotted' },
    cut: { s: 'cuts', ed: 'cut', ing: 'cutting', en: 'cut' },
    pick: { s: 'picks', ed: 'picked', ing: 'picking', en: 'picked' },
    skip: { s: 'skips', ed: 'skipped', ing: 'skipping', en: 'skipped' },
    grab: { s: 'grabs', ed: 'grabbed', ing: 'grabbing', en: 'grabbed' },
    post: { s: 'posts', ed: 'posted', ing: 'posting', en: 'posted' },
    see: { s: 'sees', ed: 'saw', ing: 'seeing', en: 'seen' },
    fall: { s: 'falls', ed: 'fell', ing: 'falling', en: 'fallen' },
    drop: { s: 'drops', ed: 'dropped', ing: 'dropping', en: 'dropped' },
    echo: { s: 'echoes', ed: 'echoed', ing: 'echoing', en: 'echoed' }
  };

  var VERB_CUES = /^(to|will|would|can|could|should|must|may|might|shall|do|does|did|don't|doesn't|didn't|won't|can't|cannot|i|you|we|they|he|she|it|who|that|and|or|then|also|often|always|never|usually|just|please|let's)$/i;
  var DETERMINERS = /^(a|an|the|this|that|these|those|my|your|our|their|his|her|its|each|every|one|no|any|some|of|for|first|last|next)$/i;
  var OPEN_CLAUSE = /^(Before|After|When|If|Because|Although|While|Once|Until|Unless|Since)\b/;

  /* ------------------------------------------------------------------ *
   * Helpers
   * ------------------------------------------------------------------ */
  function rng(seed) {
    var s = seed >>> 0 || 1;
    return function () { s ^= s << 13; s ^= s >>> 17; s ^= s << 5; return ((s >>> 0) % 10000) / 10000; };
  }
  function pick(list, r) { return list[Math.floor(r() * list.length)]; }
  function isVowel(c) { return 'aeiou'.indexOf(c) > -1; }

  function inflect(base, form) {
    if (IRREGULAR[base] && IRREGULAR[base][form]) return IRREGULAR[base][form];
    if (base.indexOf(' ') > -1) { // phrasal alternative: inflect first word only
      var parts = base.split(' ');
      parts[0] = inflect(parts[0], form);
      return parts.join(' ');
    }
    var last = base.slice(-1), prev = base.slice(-2, -1);
    if (form === 's') {
      if (/(s|x|z|ch|sh|o)$/.test(base)) return base + 'es';
      if (last === 'y' && !isVowel(prev)) return base.slice(0, -1) + 'ies';
      return base + 's';
    }
    if (form === 'ed' || form === 'en') {
      if (last === 'e') return base + 'd';
      if (last === 'y' && !isVowel(prev)) return base.slice(0, -1) + 'ied';
      return base + 'ed';
    }
    if (form === 'ing') {
      if (/ie$/.test(base)) return base.slice(0, -2) + 'ying';
      if (last === 'e' && base !== 'be' && !/ee$/.test(base)) return base.slice(0, -1) + 'ing';
      return base + 'ing';
    }
    return base;
  }

  // Build lookup: surface form -> {base, form}
  var FORMS = {};
  Object.keys(WORDS).forEach(function (base) {
    FORMS[base] = { base: base, form: 'base' };
    if (WORDS[base].p === 'v') {
      ['s', 'ed', 'ing', 'en'].forEach(function (f) {
        var surf = inflect(base, f);
        if (!FORMS[surf]) FORMS[surf] = { base: base, form: f === 'en' ? 'ed' : f };
      });
    } else if (WORDS[base].p === 'n') {
      var pl = inflect(base, 's');
      if (!FORMS[pl]) FORMS[pl] = { base: base, form: 's' };
    }
  });

  function altsFor(entry, mode) {
    if (entry[mode]) return entry[mode];
    if (mode === 'creative' || mode === 'standard') return entry.all || [];
    if (mode === 'casual') return entry.casual || entry.all || [];
    if (mode === 'academic') return entry.academic || entry.formal || entry.all || [];
    if (mode === 'formal') return entry.formal || entry.all || [];
    if (mode === 'simple') return entry.simple || [];
    return entry.all || [];
  }

  function matchCase(src, out) {
    if (src === src.toUpperCase() && src.length > 1) return out.toUpperCase();
    if (src[0] === src[0].toUpperCase()) return out.charAt(0).toUpperCase() + out.slice(1);
    return out;
  }

  /* ------------------------------------------------------------------ *
   * 3. Sentence-level transforms
   * ------------------------------------------------------------------ */
  function splitSentences(text) {
    var out = text.match(/[^.!?]+(?:[.!?]+["')\]]*|$)\s*/g) || [text];
    return out.map(function (s) { return s.trim(); }).filter(Boolean);
  }

  // "Before writing, check X." -> "Check X before writing."
  function moveLeadingClause(s) {
    var m = s.match(/^([A-Z][a-z]+ [^,]{2,60}),\s+(.+?)([.!?])$/);
    if (!m || !OPEN_CLAUSE.test(m[1]) || /\b(but|and)$/.test(m[1])) return null;
    var clause = m[1].charAt(0).toLowerCase() + m[1].slice(1);
    var main = m[2].charAt(0).toUpperCase() + m[2].slice(1);
    return main + ' ' + clause + m[3];
  }
  // "Check X because Y." -> "Because Y, check X."
  function frontTrailingClause(s) {
    var m = s.match(/^(.{15,}?)\s+(because|if|when|before|after|once|unless)\s+(.{8,}?)([.!?])$/i);
    if (!m || /,/.test(m[3])) return null;
    var main = m[1].charAt(0).toLowerCase() + m[1].slice(1);
    if (/^i\b/.test(main)) main = 'I' + main.slice(1);
    var conj = m[2].charAt(0).toUpperCase() + m[2].slice(1).toLowerCase();
    return conj + ' ' + m[3] + ', ' + main + m[4];
  }
  // Split sentences longer than ~26 words at a natural joint.
  function splitLong(s) {
    var words = s.split(/\s+/);
    if (words.length < 26) return [s];
    var joints = [/;\s+/, /,\s+(but|so|and|which means)\s+/i, /,\s+which\s+/i];
    for (var i = 0; i < joints.length; i++) {
      var m = s.match(joints[i]);
      if (m && m.index > 40 && m.index < s.length - 30) {
        var first = s.slice(0, m.index).replace(/[,;]$/, '') + '.';
        var rest = s.slice(m.index + m[0].length);
        var lead = (m[1] || '').toLowerCase();
        if (lead === 'which' || lead === 'which means') rest = 'This ' + (lead === 'which means' ? 'means ' : '') + rest;
        else if (lead === 'but') rest = 'But ' + rest;
        else if (lead === 'so') rest = 'So ' + rest;
        rest = rest.charAt(0).toUpperCase() + rest.slice(1);
        return [first, rest];
      }
    }
    return [s];
  }

  var CONTRACT = [[/\bdo not\b/gi, "don't"], [/\bdoes not\b/gi, "doesn't"], [/\bdid not\b/gi, "didn't"], [/\bwill not\b/gi, "won't"], [/\bcannot\b/gi, "can't"], [/\bis not\b/gi, "isn't"], [/\bare not\b/gi, "aren't"], [/\bwould not\b/gi, "wouldn't"], [/\bshould not\b/gi, "shouldn't"], [/\bcould not\b/gi, "couldn't"], [/\bit is\b/gi, "it's"], [/\bthat is\b/gi, "that's"], [/\byou are\b/gi, "you're"], [/\bwe are\b/gi, "we're"], [/\bthey are\b/gi, "they're"], [/\bI am\b/g, "I'm"]];
  var EXPAND = [[/\bdon't\b/gi, 'do not'], [/\bdoesn't\b/gi, 'does not'], [/\bdidn't\b/gi, 'did not'], [/\bwon't\b/gi, 'will not'], [/\bcan't\b/gi, 'cannot'], [/\bisn't\b/gi, 'is not'], [/\baren't\b/gi, 'are not'], [/\bwouldn't\b/gi, 'would not'], [/\bshouldn't\b/gi, 'should not'], [/\bit's\b/gi, 'it is'], [/\bthat's\b/gi, 'that is'], [/\byou're\b/gi, 'you are'], [/\bwe're\b/gi, 'we are'], [/\bthey're\b/gi, 'they are'], [/\bI'm\b/g, 'I am']];
  function applyPairs(s, pairs) {
    pairs.forEach(function (p) { s = s.replace(p[0], function (m) { return matchCase(m, p[1]); }); });
    return s;
  }

  /* ------------------------------------------------------------------ *
   * 4. Core paraphrase
   * ------------------------------------------------------------------ */
  function protectSpans(text) {
    // Quoted text, URLs, emails, numbers with units are never touched.
    var store = [];
    var out = text.replace(/("[^"]+"|“[^”]+”|https?:\/\/\S+|\S+@\S+\.\S+)/g, function (m) {
      store.push(m); return '\u0000' + (store.length - 1) + '\u0000';
    });
    return { text: out, restore: function (t) { return t.replace(/\u0000(\d+)\u0000/g, function (_, i) { return store[+i]; }); } };
  }

  function rewritePhrases(s, mode, r, counter) {
    PHRASES.forEach(function (rule) {
      var re = new RegExp('\\b' + rule[0].replace(/[-]/g, '\\-') + '\\b', 'gi');
      s = s.replace(re, function (m) {
        var alts = rule[1][mode] || rule[1].all;
        if (!alts || !alts.length) return m;
        var choice = pick(alts, r);
        if (choice.toLowerCase() === m.toLowerCase()) return '\u0001' + m + '\u0002';
        counter.phr += m.split(/\s+/).length;
        return '\u0001' + matchCase(m, choice) + '\u0002'; // mark as done
      });
    });
    return s;
  }

  function rewriteWords(s, mode, r, counter, rate) {
    var tokens = s.split(/(\s+)/);
    var prevWord = '';
    var inDone = false;
    for (var i = 0; i < tokens.length; i++) {
      var t = tokens[i];
      if (/^\s+$/.test(t) || !t) continue;
      if (t.indexOf('\u0001') > -1) inDone = true;
      var wasDone = inDone;
      if (t.indexOf('\u0002') > -1) inDone = false;
      if (wasDone || t.indexOf('\u0000') > -1) { prevWord = t.replace(/[^\w']/g, ''); continue; }
      var m = t.match(/^([^A-Za-z]*)([A-Za-z][A-Za-z'-]*)([^A-Za-z]*)$/);
      if (!m) { prevWord = ''; continue; }
      var word = m[2], lower = word.toLowerCase();
      // Proper noun mid-sentence (capitalised, not first word): leave it.
      var isFirst = i === 0 || /[.!?]["')]?$/.test(tokens[i - 2] || '');
      if (!isFirst && /^[A-Z]/.test(word)) { prevWord = lower; continue; }
      var f = FORMS[lower];
      if (f && r() < rate) {
        var entry = WORDS[f.base];
        var ok = true;
        if (entry.amb && entry.p === 'v') ok = VERB_CUES.test(prevWord) && !DETERMINERS.test(prevWord);
        if (entry.amb && entry.p === 'n') ok = DETERMINERS.test(prevWord);
        if (entry.p === 'v' && DETERMINERS.test(prevWord) && f.form === 'base') ok = false;
        if (entry.noTo && /^to\b/i.test(tokens[i + 2] || '')) ok = false;
        if (entry.p === 'n' && /^(s|es)$/.test(f.form) === false && f.form === 's' && entry.p !== 'n') ok = false;
        var alts = altsFor(entry, mode).filter(function (a) { return a !== f.base; });
        if (mode === 'simple') alts = alts.filter(function (a) { return a.length <= f.base.length + 1; });
        if (ok && alts.length) {
          var alt = pick(alts, r);
          var out = f.form === 'base' ? alt : inflect(alt, f.form);
          if (f.form === 's' && entry.p === 'n') { var ws = alt.split(' '); ws[ws.length - 1] = inflect(ws[ws.length - 1], 's'); out = ws.join(' '); }
          // a/an agreement
          if (/^(a|an)$/i.test(prevWord) && i >= 2) {
            var art = isVowel(out.charAt(0).toLowerCase()) ? 'an' : 'a';
            tokens[i - 2] = tokens[i - 2].replace(/^(a|an)$/i, function (x) { return matchCase(x, art); });
          }
          tokens[i] = m[1] + matchCase(word, out) + m[3];
          counter.words++;
        }
      }
      prevWord = lower;
    }
    return tokens.join('');
  }

  function paraphrase(text, mode, seed) {
    mode = mode || 'standard';
    var r = rng(seed || (Date.now() & 0xffff));
    var rate = { standard: 0.75, creative: 0.95, simple: 0.9, formal: 0.8, casual: 0.8, academic: 0.8 }[mode] || 0.75;
    var prot = protectSpans(text.replace(/\r\n/g, '\n'));
    var paragraphs = prot.text.split(/\n{2,}/);
    var counter = { words: 0, phr: 0, restructured: 0 };
    var sentenceCount = 0;

    var outParas = paragraphs.map(function (para) {
      var sentences = splitSentences(para.replace(/\n/g, ' '));
      sentenceCount += sentences.length;
      var out = [];
      sentences.forEach(function (s, idx) {
        // structure first
        if (mode === 'simple' || mode === 'standard' || mode === 'creative') {
          var parts = splitLong(s);
          if (parts.length > 1) counter.restructured++;
          s = parts.join(' ');
        }
        if (mode !== 'simple') {
          var moved = null;
          var chance = mode === 'creative' ? 0.9 : 0.55;
          if (r() < chance) moved = moveLeadingClause(s) || (idx % 2 === 1 ? frontTrailingClause(s) : null);
          if (moved) { s = moved; counter.restructured++; }
        }
        s = rewritePhrases(s, mode, r, counter);
        s = rewriteWords(s, mode, r, counter, rate);
        if (mode === 'casual' || mode === 'simple' || mode === 'creative') s = applyPairs(s, CONTRACT);
        if (mode === 'formal' || mode === 'academic') s = applyPairs(s, EXPAND);
        out.push(s.replace(/[\u0001\u0002]/g, ''));
      });
      return out.join(' ');
    });

    var output = prot.restore(outParas.join('\n\n')).replace(/[ \t]+/g, ' ').replace(/ ([,.;:!?])/g, '$1').trim();
    var inWords = (text.match(/\S+/g) || []).length;
    return {
      text: output,
      changed: counter.words + counter.phr,
      total: inWords,
      sentences: sentenceCount,
      restructured: counter.restructured,
      copiedPhrases: overlap(text, output)
    };
  }

  // Share of the output's 5-word sequences that also appear in the input.
  function overlap(a, b) {
    var w = function (s) { return (s.toLowerCase().match(/[a-z0-9']+/g) || []); };
    var A = w(a), B = w(b), set = {}, n = 5, hit = 0, tot = 0;
    for (var i = 0; i + n <= A.length; i++) set[A.slice(i, i + n).join(' ')] = 1;
    for (var j = 0; j + n <= B.length; j++) { tot++; if (set[B.slice(j, j + n).join(' ')]) hit++; }
    return tot ? Math.round((hit / tot) * 100) : 0;
  }

  var api = { paraphrase: paraphrase, overlap: overlap, inflect: inflect };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  root.BFParaphraser = api;

  /* ------------------------------------------------------------------ *
   * 5. Page wiring (same element IDs as the existing tool page)
   * ------------------------------------------------------------------ */
  if (typeof document === 'undefined') return;

  var inputEl, outputEl, currentMode = 'standard', runCount = 0;
  function $(id) { return document.getElementById(id); }

  function init() {
    inputEl = $('inputText'); outputEl = $('outputText');
    if (!inputEl || !outputEl) { setTimeout(init, 200); return; }
    inputEl.addEventListener('input', function () {
      var v = this.value.trim();
      $('wordCount').textContent = v ? v.split(/\s+/).length : 0;
      $('charCount').textContent = this.value.length;
    });
    // Extra stat + note, injected once so the page HTML needs no edits.
    var bar = $('statsBar');
    if (bar && !$('statOriginality')) {
      var item = document.createElement('div');
      item.className = bar.firstElementChild ? bar.firstElementChild.className : '';
      item.innerHTML = 'Phrases kept: <strong id="statOriginality">0%</strong>';
      bar.appendChild(item);
      var note = document.createElement('p');
      note.id = 'paraNote';
      note.style.cssText = 'margin:10px 0 0;font-size:14px;line-height:1.5;display:none';
      bar.parentNode.insertBefore(note, bar.nextSibling);
    }
    var label = $('progressLabel');
    if (label) label.textContent = 'Rewriting with AI...';
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();

  window.toggleFaq = function (btn) { btn.parentElement.classList.toggle('open'); };

  window.setMode = function (btn, mode) {
    currentMode = mode;
    var btns = $('modeRow').getElementsByTagName('button');
    for (var i = 0; i < btns.length; i++) btns[i].className = 'mode-btn';
    btn.className = 'mode-btn active';
  };

  /* AI rewrite (free Pollinations API) with the rule engine as fallback. */
  var AI_URL = 'https://text.pollinations.ai/openai', AI_GAP = 16000, lastAI = 0, busy = false;
  var MODE_GUIDE = {
    standard: 'Rewrite in clear, natural English. Change wording and sentence structure; keep the same tone and length.',
    formal: 'Rewrite in a formal, professional tone suitable for business documents. No contractions.',
    casual: 'Rewrite in a relaxed, conversational tone, as if explaining to a friend. Use contractions.',
    creative: 'Rewrite with the most change: restructure sentences, vary rhythm and use fresh phrasing, while keeping the meaning.',
    simple: 'Rewrite in plain English that a 12-year-old could follow. Short sentences, common words.',
    academic: 'Rewrite in a precise academic register suitable for an essay or paper. No contractions, no filler.'
  };
  function aiPrompt(mode) {
    return 'You are a paraphrasing tool. ' + MODE_GUIDE[mode] +
      ' Rules: keep every fact, number, unit, measurement, name, brand and product name exactly as written. ' +
      'Do not add information, opinions or examples, and do not remove any. Use British English spelling. ' +
      'Avoid the words moreover, furthermore, additionally, delve, crucial. ' +
      'Keep the same paragraph breaks. Reply with the rewritten text only, no preamble or notes.';
  }
  function chunks(text) {
    var paras = text.split(/\n\s*\n/), out = [], cur = '';
    paras.forEach(function (p) {
      var cand = cur ? cur + '\n\n' + p : p;
      if (cur && cand.split(/\s+/).length > 600) { out.push(cur); cur = p; } else cur = cand;
    });
    if (cur) out.push(cur);
    return out;
  }
  function wait(ms) { return new Promise(function (r) { setTimeout(r, ms); }); }
  function callAI(text, mode, tries) {
    var gap = AI_GAP - (Date.now() - lastAI), p = gap > 0 ? wait(gap) : Promise.resolve();
    return p.then(function () {
      lastAI = Date.now();
      var ctrl = typeof AbortController !== 'undefined' ? new AbortController() : null;
      var timer = setTimeout(function () { if (ctrl) ctrl.abort(); }, 60000);
      return fetch(AI_URL, {
        method: 'POST', headers: { 'Content-Type': 'application/json' }, signal: ctrl ? ctrl.signal : undefined,
        body: JSON.stringify({ model: 'openai', referrer: 'brightlyfuture.co.uk', private: true,
          seed: Math.floor(Math.random() * 1e9),
          messages: [{ role: 'system', content: aiPrompt(mode) }, { role: 'user', content: text }] })
      }).then(function (r) {
        clearTimeout(timer);
        if ((r.status === 429 || r.status === 402) && tries < 2) return callAI(text, mode, tries + 1);
        if (!r.ok) throw new Error('AI service returned ' + r.status);
        return r.json();
      }).then(function (d) {
        if (typeof d === 'string') return d;
        var t = d && d.choices && d.choices[0] && d.choices[0].message && d.choices[0].message.content;
        if (!t || !t.trim()) throw new Error('Empty AI reply');
        return t.trim().replace(/^["“]|["”]$/g, '');
      });
    });
  }
  function wordDiff(a, b) {
    var A = a.toLowerCase().match(/[\w'’-]+/g) || [], B = b.toLowerCase().match(/[\w'’-]+/g) || [];
    if (A.length * B.length > 4e6) return { changed: B.length, total: A.length };
    var prev = new Array(B.length + 1).fill(0), cur;
    for (var i = 1; i <= A.length; i++) {
      cur = [0];
      for (var j = 1; j <= B.length; j++) cur[j] = A[i - 1] === B[j - 1] ? prev[j - 1] + 1 : Math.max(prev[j], cur[j - 1]);
      prev = cur;
    }
    return { changed: B.length - prev[B.length], total: A.length };
  }
  function sentenceCount(t) { return (t.match(/[^.!?]+[.!?]+(\s|$)/g) || [t]).length; }

  function show(src, out, stats, via) {
    outputEl.value = out;
    var ow = out.trim() ? out.trim().split(/\s+/).length : 0;
    $('outWordCount').textContent = ow;
    $('outCharCount').textContent = out.length;
    $('statChanged').textContent = stats.changed;
    $('statRate').textContent = Math.min(100, Math.round((stats.changed / Math.max(1, stats.total)) * 100)) + '%';
    $('statSentences').textContent = stats.sentences + (stats.restructured ? ' (' + stats.restructured + ' restructured)' : '');
    var names = { standard: 'Standard', formal: 'Formal', casual: 'Casual', creative: 'Creative', simple: 'Simple', academic: 'Academic' };
    $('statMode').textContent = (names[currentMode] || 'Standard') + (via === 'ai' ? ' (AI)' : ' (basic)');
    var kept = overlap(src, out), o = $('statOriginality'), note = $('paraNote');
    if (o) o.textContent = kept + '%';
    if (note) {
      note.style.display = '';
      var msg = kept > 40
        ? 'Over 40% of 5-word phrases match your original. Click Paraphrase again for a new version, try Creative mode, or rewrite key sentences yourself. If this is someone else\'s text, cite the source.'
        : 'Read the result against your original before using it: check names, numbers and "not". If the ideas came from someone else, cite the source.';
      if (via === 'fallback') msg = 'The AI service is busy, so this is the basic word-swap version, which changes far less. Try again in a minute for a full rewrite. ' + msg;
      note.textContent = msg;
    }
  }
  function done() {
    busy = false;
    $('progressWrap').style.display = 'none';
    $('paraphraseBtn').disabled = false;
    $('statsBar').style.display = '';
  }

  window.paraphraseText = function () {
    if (busy) return;
    var text = inputEl.value.trim();
    if (!text) { alert('Please paste some text to paraphrase.'); return; }
    if (text.split(/\s+/).length < 3) { alert('Please paste at least 3 words.'); return; }
    busy = true;
    $('paraphraseBtn').disabled = true;
    $('progressWrap').style.display = '';
    $('statsBar').style.display = 'none';
    var fill = $('progressFill'), label = $('progressLabel'), mode = currentMode;
    var parts = chunks(text), out = [], k = 0;
    fill.style.width = '10%';
    function next() {
      if (k >= parts.length) {
        var res = out.join('\n\n'), d = wordDiff(text, res);
        fill.style.width = '100%';
        show(text, res, { changed: d.changed, total: d.total, sentences: sentenceCount(res) }, 'ai');
        return done();
      }
      var waitS = Math.max(0, Math.ceil((AI_GAP - (Date.now() - lastAI)) / 1000));
      label.textContent = parts.length > 1
        ? 'Rewriting part ' + (k + 1) + ' of ' + parts.length + (waitS && k ? ' (free AI limit: about ' + waitS + 's between parts)' : '') + '...'
        : (waitS ? 'Waiting ' + waitS + 's for the free AI service...' : 'Rewriting with AI...');
      return callAI(parts[k], mode, 0).then(function (t) {
        out.push(t); k++; fill.style.width = Math.round(10 + 85 * k / parts.length) + '%'; return next();
      });
    }
    next().catch(function () {
      runCount++;
      var res = paraphrase(text, mode, (Date.now() + runCount * 7919) & 0x7fffffff);
      fill.style.width = '100%';
      show(text, res.text, res, 'fallback');
      done();
    });
  };

  window.copyOutput = function () {
    var text = outputEl.value;
    if (!text) { alert('Nothing to copy. Paraphrase some text first.'); return; }
    var done = function () { var t = $('toast'); if (!t) return; t.classList.add('show'); setTimeout(function () { t.classList.remove('show'); }, 2000); };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(done);
    else { var ta = document.createElement('textarea'); ta.value = text; document.body.appendChild(ta); ta.select(); document.execCommand('copy'); document.body.removeChild(ta); done(); }
  };

  window.downloadOutput = function () {
    var text = outputEl.value;
    if (!text) { alert('Nothing to download. Paraphrase some text first.'); return; }
    var a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([text], { type: 'text/plain' }));
    a.download = 'paraphrased-text.txt';
    document.body.appendChild(a); a.click(); document.body.removeChild(a);
  };

  window.clearAll = function () {
    inputEl.value = ''; outputEl.value = '';
    inputEl.dispatchEvent(new Event('input'));
    $('outWordCount').textContent = '0'; $('outCharCount').textContent = '0';
    $('statsBar').style.display = 'none'; $('progressWrap').style.display = 'none';
    var n = $('paraNote'); if (n) n.style.display = 'none';
  };
})(typeof window !== 'undefined' ? window : this);
