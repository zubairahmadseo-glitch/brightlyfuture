# Audit of the 8 Live Exercise Pages — Errors and Exact Fixes

Checked on 29 Oct 2026 against each page's GIF, the research cited on the page, and standard exercise technique.
Format: **Field → what is wrong → paste this instead.**

---

## Site-wide issues (fix first)

1. **Exercise pages are not in the sitemap.** `sitemap_index.xml` lists only `post-sitemap.xml` and `page-sitemap.xml`. The `exercises` post type is missing, so Google is not being told about any exercise page.
   **Fix:** Rank Math → Titles & Meta → (Exercises post type) → enable "Include in Sitemap" (Rank Math → Sitemap Settings → Post Types). The post type must also be public.
2. **Calf raise page slug is `/exercises/992896/`.** Change the slug to `barbell-standing-calf-raise` and add a 301 redirect from `/exercises/992896/` (Rank Math → Redirections).
3. **"Related Training Articles" is empty** on the Dumbbell Hammer Curl and Dumbbell Biceps Curl pages. Add 3 links, for example `/how-to-train-deltoids-and-biceps-with-dumbbells/`, `/how-many-reps-and-sets-for-muscle-growth/`, `/what-is-progressive-overload/`.
4. **No links to workout plans yet.** None of the 15 workout plans are live on the sitemap. Once they publish, add the plan links to each exercise page, and link each plan back to the exercise pages.

---

## 1. Barbell Lying Triceps Extension — `/exercises/barbell-lying-triceps-extension/`

**GIF check:** The GIF starts with the arms vertical over the **shoulders/upper chest** and lowers the bar to the **forehead/top of the head**. The page says "over your eyes" and "behind your head".

| Field | Problem | Replace with |
|---|---|---|
| Quick Answer | Says lower "behind your head", which is not what the GIF shows | The barbell lying triceps extension is an isolation lift that targets all three heads of the triceps. Lie flat on a bench, hold a barbell over your shoulders with arms straight, and bend only at the elbows to lower it toward your forehead. Press back up. Use 3 sets of 8 to 12 reps. |
| Step 2 | "positioned over your eyes" — the GIF shows the bar over the shoulders | Press the bar up so your arms are straight and vertical over your shoulders. |
| Step 4 | "behind your head until your forearms touch your biceps" | Lower the bar in a slow, controlled arc toward your forehead or just past it, keeping your upper arms still. |
| Tip 2 "Lower Behind the Head…" | Says this "extends the shoulder". That is wrong. Letting the upper arms angle back toward the head is shoulder **flexion**, and that is what lengthens the long head. | **Let the Upper Arms Angle Back Slightly for More Stretch:** Allowing the upper arms to tilt slightly back toward your head increases shoulder flexion, which places the long head of the triceps under more stretch. Keep the movement at the elbows. |
| Tip 4 "Set the Bar Over Your Eyes…" | Contradicts the GIF, and "reduces results" is unsupported | **Start with the Bar Over Your Shoulders:** Begin with your arms vertical over your shoulders so the triceps hold the weight in a stable position before each rep. |
| Modification "Harder — Decline Lying Triceps Extension" | Wrong. A decline bench **reduces** shoulder flexion relative to the torso, so it gives the long head **less** stretch, not more. | **🔼 Harder — Incline Lying Triceps Extension:** Performing the movement on a low incline bench angles the arms further overhead relative to your torso, placing the long head of the triceps under a greater stretch. |
| FAQ 1 | Contradicts itself (says "same lift" when behind the head, then "skull crusher" means to the forehead) | **Is the barbell lying triceps extension the same as a skull crusher?** Yes. "Skull crusher" is the common gym name for the lying triceps extension. Some lifters lower the bar to the forehead and others just behind the head; both are the same exercise. |
| FAQ 2 | "straight bar preferred for maximum long head stretch" is unsupported | **Should I use a straight bar or an EZ bar?** Both work. Many lifters find the angled EZ bar grip easier on the wrists and elbows, so it is a common choice. |
| Secondary muscle "Forearm Flexors" | Acceptable. No change needed. | — |

---

## 2. Barbell Incline Bench Press — `/exercises/barbell-incline-bench-press/`

| Field | Problem | Replace with |
|---|---|---|
| Step 5 | "press… slightly over your face" — the GIF finishes with the bar over the shoulders | Press the bar back up until your arms lock out with the bar directly over your shoulders. |
| Mistake 5 "Pressing Toward the Ceiling, Not the Face" | Tells readers to finish "above your eyes". The stable lockout is over the shoulder joint. | **Letting the Bar Drift Toward Your Stomach:** On an incline, the bar should finish over your shoulders. Pressing it forward toward your stomach puts the weight in a weaker position and is harder to control. |
| Tip 1 "Confirm the Bench Angle" | Says "between 30 and 45 degrees", while the FAQ and the mistake say 30 degrees is best. Make it consistent. | **Confirm the Bench Angle First:** Not every bench marks the exact angle. Aim for about 30 degrees and keep it the same each week so you can track progress. |
| FAQ 1 | "Research-backed" with no source | A 30-degree incline is a good default. A 2020 study by Rodríguez-Ridao and colleagues (Int J Environ Res Public Health) found the upper chest was most active at 30 degrees, while angles above 45 degrees shifted activity to the front delts. Link: https://pmc.ncbi.nlm.nih.gov/articles/PMC7579505/ |
| FAQ 5 | "20 to 30 percent less weight" — no source | Most lifters press less weight on an incline than on a flat bench because the front delts take a larger share of the work. Start lighter and build up. |

---

## 3. Barbell Bench Press — `/exercises/barbell-bench-press/`

| Field | Problem | Replace with |
|---|---|---|
| **How-To Steps** | **The section is completely empty on the live page.** | 1. **Set up under the bar** — Lie on the bench with your eyes directly under the bar, feet flat on the floor. 2. **Set your grip** — Grip the bar slightly wider than shoulder-width, wrists stacked over your forearms. 3. **Pin your shoulder blades** — Pull your shoulder blades back and down into the bench and keep a small natural arch. 4. **Unrack** — Lift the bar out of the rack and hold it with straight arms over your shoulders. 5. **Lower to mid-chest** — Lower the bar under control to your mid or lower chest, with elbows about 45–70 degrees from your torso. 6. **Press up** — Press the bar back up and slightly back until your arms lock out over your shoulders. |
| Modification "Close-Grip Bench Press" | "shifts load to… inner chest" — the idea that you can target the "inner chest" is a myth. | Narrow your grip to about shoulder-width. This shifts more of the work to the triceps and builds lockout strength. |
| FAQ 1 | "Most untrained women start with a lighter 15 to 25-pound bar" — 15-lb bars are not standard, and the claim has no source | **How much should a beginner bench press?** Start with a weight you can lift for 8–10 controlled reps. For many beginners this is the empty 20 kg (45 lb) bar or a lighter fixed barbell. Add 1–2.5 kg (2.5–5 lb) when all sets feel solid. |
| FAQ 4 | "targets the mid and lower chest" — the 2020 Rodríguez-Ridao study supports this, so add the source | Flat bench produces the highest mid and lower chest activity, while about 30 degrees produces the highest upper chest activity (Rodríguez-Ridao et al., 2020). Include both over a training week. |

---

## 4. Barbell Standing Calf Raise — `/exercises/992896/`

| Field | Problem | Replace with |
|---|---|---|
| Slug | `992896` | `barbell-standing-calf-raise`, plus a 301 redirect |
| Quick Answer | "soleus working as a secondary stabiliser" — the soleus is a prime mover in plantar flexion, not a stabiliser. "The heel drives upward through the ball of the foot" is unclear. | The barbell standing calf raise is a calf exercise performed standing with a barbell across your upper back. Keeping the knees straight makes the gastrocnemius the main mover, with the soleus assisting. Raise your heels as high as you can, then lower for a full stretch. Use 3–4 sets of 10–15 reps. |
| Secondary muscle "Soleus" | Fine as secondary, but do not call it a stabiliser anywhere | Soleus — assists plantar flexion; it works in every calf raise but contributes less when the knee is straight. |
| Tip 2 (Cresswell) | Wrong journal and an invented threshold. The paper is in **Experimental Brain Research** (not Experimental Physiology) and does not give a "20–35 degree" figure. | Knee position changes which calf muscle does most of the work. Cresswell and colleagues (1995, Experimental Brain Research) found gastrocnemius activity dropped as the knee bent, while soleus activity stayed the same. Straight knees bias the gastrocnemius; the seated calf raise with bent knees biases the soleus. Link: https://pubmed.ncbi.nlm.nih.gov/7498381/ |
| Tip 1 (Gentil 2020) | Study is real and correctly summarised. Add the link. | Link: https://www.mdpi.com/1660-4601/17/24/9487 |
| Tip 3 & FAQ 2 | "The gastrocnemius recovers faster… responds better to higher frequency" — no source | Training calves 2–3 times per week works well for most people and makes it easier to spread the weekly sets. If calves are lagging, adding a second weekly session is a simple first step. |
| Tip 4 / Mistake 2 | "Lifters who train… without a platform… are almost always missing this range" — overclaim | Standing on a step or plate lets the heels drop below the toes and trains the calf through a longer range. Kassiano et al. (2023) found training in the stretched part of the calf raise produced more gastrocnemius growth than training in the shortened part. |
| Mistake 3 | "The gastrocnemius is a relatively small muscle and fatigues faster than lifters expect" — unsupported | Remove that sentence. Keep: "If the ankle rolls outward or the heel drops passively, the load is too heavy." |
| Modification "Harder — Barbell Seated Calf Raise" | The page itself says it is "not a progression". It is mislabeled. | **🔼 Harder — Paused Standing Calf Raise:** Hold the bottom stretch for 2 seconds and the top for 1 second on every rep. This removes the bounce from the Achilles tendon and makes the calves do all the work. |

---

## 5. Dumbbell Bench Press — `/exercises/dumbbell-bench-press/`

| Field | Problem | Replace with |
|---|---|---|
| Tip 3 (Solstad 2020) | **Misquoted study.** Solstad et al. (2020, JSSM) compared the **barbell bench press with dumbbell flyes**, not dumbbell presses, and said nothing about moment arms or the dumbbell press bottom position. | Saeterbakken and colleagues (2011, Journal of Sports Sciences) compared the barbell, Smith machine, and dumbbell bench press. Chest and front delt activity were similar across all three, while 1-RM was about 17% lower with dumbbells than with a barbell. Use dumbbells for range and balance, and a barbell for maximum load. Link: https://pubmed.ncbi.nlm.nih.gov/21225489/ |
| Mistake 1 & Tip 2 | "load transfers to the anterior deltoid and away from the pectoralis major" — not supported. The problem with fully flared elbows is extra shoulder stress. | **Flaring elbows to 90 degrees:** Fully flared elbows put the front of the shoulder in a more stressful position. Keep the elbows about 45–75 degrees from the torso. |
| Mistake 5 | "most common injury mechanism" — no source | **Dropping the dumbbells to the side after the set:** Letting heavy dumbbells fall out to the sides with the arms stretched can strain the shoulders. Bring them back to your thighs and sit up. |
| Tip 4 | "reduces long-term impingement risk" — no evidence | Program the dumbbell bench press early in a push session, when you are fresh. Balancing pressing with rowing across the week keeps your training balanced. |
| Modification "Dumbbell Tempo Bench Press" | "Research consistently supports eccentric loading as a primary driver of hypertrophy" — overclaim. A meta-analysis (Schoenfeld et al., 2015) found similar growth across rep durations from 0.5 to 8 seconds. | **🔼 Harder — Dumbbell Tempo Bench Press:** Lower each rep over 3–4 seconds. The slower lowering makes the same weight harder and builds control. Link: https://pubmed.ncbi.nlm.nih.gov/25601394/ |
| Tip 1 | "NASM Exercise Library" with no link | Remove the citation or link to a specific NASM page. |
| FAQ 4 | "women 6–10 kg, men 10–16 kg" — no source | Start with a weight you can press for 10–12 controlled reps with a full range of motion. For many beginners that is a light pair of dumbbells, and the right weight varies widely. |

---

## 6. Barbell Curl — `/exercises/barbell-curl/`

| Field | Problem | Replace with |
|---|---|---|
| Mistake 4 | "The eccentric phase is a primary driver of muscle protein synthesis" — overclaim | **Rushing the lowering phase:** Dropping the bar fast loses control and reduces time under tension. Lower over 2–3 seconds. |
| Step 5 | "The eccentric phase is a primary driver of hypertrophy" — overclaim | Lower the bar slowly over 2–3 seconds until your arms are almost straight. |
| Tip 2 & FAQ 2 (Marcolin 2018) | The study's main finding is that the **EZ bar produced higher activation than the dumbbell curl**. The straight bar vs EZ bar difference was small. Saying "no significant difference" leaves out the main result. | Marcolin and colleagues (2018, PeerJ) found only small differences in biceps activation between the straight bar and the EZ bar, and higher activation with the EZ bar than with dumbbells. Choose between the two bars based on wrist comfort. Link: https://peerj.com/articles/5165/ |
| Modification "Barbell Drag Curl" | "stretches the long head at the start and removes anterior deltoid involvement entirely" — incorrect. The elbows move back during the curl, so the long head is not more stretched at the start. | **🔼 Harder — Barbell Drag Curl:** Drag the bar up along the front of your body while pulling the elbows back. This stops the front delts from helping and keeps the biceps working hard at the top. |
| Mistake 3 | "shifts force… to the forearm tendons" — vague | **Bending the wrists back:** Letting the wrists extend under load strains them and reduces control. Keep them straight. |

---

## 7. Dumbbell Hammer Curl — `/exercises/dumbbell-hammer-curl/`

| Field | Problem | Replace with |
|---|---|---|
| Subtitle | "An alternating curl…" — hammer curls can be done alternating or with both arms together | A dumbbell curl with a neutral (thumbs-up) grip that targets the brachialis and brachioradialis more than a standard biceps curl. |
| Mistake 2 "Curling both arms simultaneously" | **Wrong.** Curling both arms together is a normal way to do hammer curls, not a mistake. | **Letting the dumbbells swing forward:** Swinging the dumbbells in front of you uses momentum. Keep them moving straight up and down at your sides. |
| Tip 1 | **Copy-paste error.** It repeats Mistake 5 word for word. | **Keep the Thumbs Up the Whole Time:** Hold the neutral grip from bottom to top so the brachialis and brachioradialis stay loaded. |
| Tip 2 "use wrist straps" | Grip rarely limits a hammer curl, and straps make no sense for an exercise used to build the forearms | Remove. Replace with: **Try Cross-Body Hammer Curls for Variety:** Curling the dumbbell toward the opposite shoulder is a common variation that some lifters find more comfortable. |
| Modification "Cross-Body Hammer Curl" | "increases range of motion and places the brachialis under greater stretch" — unsupported | Curling the dumbbell across your body toward the opposite shoulder is a variation many lifters find more comfortable on the wrist and elbow. |
| FAQ 2 | "Alternating is the standard form… Bilateral hammer curls are less common" — incorrect | Both are fine. Alternating gives each arm a short rest and makes it easier to stay strict; curling both arms together saves time. |
| FAQ 3 | **Factually wrong:** "the brachioradialis… is a larger and mechanically stronger muscle than the biceps brachii". The biceps is the larger muscle. | **Why can I lift more on hammer curls?** With a neutral grip, the brachioradialis is in a strong position, and the brachialis and biceps still contribute, so most people can handle a little more weight than with a palms-up curl. |
| Related Training Articles | Empty | Add 3 links (see site-wide issue 3). |

---

## 8. Dumbbell Biceps Curl — `/exercises/dumbbell-biceps-curl/`

| Field | Problem | Replace with |
|---|---|---|
| Mistake 4 | "NSCA research confirms eccentric loading is a primary driver of hypertrophy" — the NSCA attribution has no source and the claim is overstated | **Rushing the lowering phase:** Dropping the weight fast loses control and tension. Lower over 2–3 seconds on every rep. |
| Step 5 | "That eccentric phase is where a significant portion of muscle stimulus occurs" — overclaim, and uses the banned word "significant" | Return the dumbbells slowly over 2–3 seconds to full extension. Do not bounce or cut the range short. |
| Tip 2 | "slight external rotation of the wrist… puts the short head in a more mechanically advantageous position" — wrong terms and unsupported. The wrist does not externally rotate; the forearm **supinates**. | **Keep Turning the Palms Up:** The biceps both bend the elbow and turn the palm up (supination). Keeping the palms fully turned up, with the little finger slightly higher, keeps the biceps working throughout the rep. |
| FAQ 2 & FAQ 4 | **Formatting bug:** stray `:` at the start (": Are dumbbell curls…" and ":  Not recommended.") | Delete the leading colon in both. |
| FAQ 4 | "Biceps need 48–72 hours to recover" — commonly stated but no source | Training biceps hard every day leaves little time to recover. Two or three sessions per week with a rest day in between works well for most lifters. |
| FAQ 5 | "women 5–8 kg, men 8–12 kg" — no source; 8–12 kg is heavy for many untrained men | Start with a weight you can curl for 10–12 controlled reps without swinging. If the last two reps break form, go lighter. |
| Related Training Articles | Empty | Add 3 links (see site-wide issue 3). |

---

## Citations verified (OK to keep or link)

| Study | Verified source |
|---|---|
| Gentil et al. 2020 — calf raise vs leg press EMG | https://www.mdpi.com/1660-4601/17/24/9487 |
| Cresswell, Löscher, Thorstensson 1995 — Exp Brain Res (not Exp Physiology) | https://pubmed.ncbi.nlm.nih.gov/7498381/ |
| Marcolin et al. 2018 — PeerJ, three curl variants | https://peerj.com/articles/5165/ |
| Rodríguez-Ridao et al. 2020 — five bench inclinations | https://pmc.ncbi.nlm.nih.gov/articles/PMC7579505/ |
| Saeterbakken et al. 2011 — barbell vs Smith vs dumbbell bench (J Sports Sci) | https://pubmed.ncbi.nlm.nih.gov/21225489/ |
| Schoenfeld et al. 2015 — repetition duration meta-analysis | https://pubmed.ncbi.nlm.nih.gov/25601394/ |
| Solstad et al. 2020 — **barbell bench vs dumbbell FLYES** (do not use for dumbbell press claims) | https://pmc.ncbi.nlm.nih.gov/articles/PMC7675616/ |
