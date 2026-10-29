<?php
/**
 * Single Exercise Template (v1.2.0 — layout matches the approved preview page)
 * All content comes from the plugin fields; nothing is hard-coded per exercise.
 */
if ( ! defined('ABSPATH') ) exit;

$post_id    = get_the_ID();
$title      = get_the_title();
$subtitle   = get_post_meta($post_id,'_em_subtitle',true);
$tags_raw   = get_post_meta($post_id,'_em_tags',true);
$tags       = $tags_raw ? array_filter(array_map('trim', explode(',', $tags_raw))) : [];
$gif_url    = get_post_meta($post_id,'_em_gif_url',true);
$gif_alt    = get_post_meta($post_id,'_em_gif_alt',true) ?: $title . ' exercise demonstration';
$qa         = get_post_meta($post_id,'_em_quick_answer',true);
$primary    = em_get_list_meta($post_id,'_em_primary_muscles');
$secondary  = em_get_list_meta($post_id,'_em_secondary_muscles');
$steps      = em_get_list_meta($post_id,'_em_steps');
$sets_reps  = em_get_list_meta($post_id,'_em_sets_reps');
$mistakes   = em_get_list_meta($post_id,'_em_mistakes');
$tips       = em_get_list_meta($post_id,'_em_tips');
$mods       = em_get_list_meta($post_id,'_em_mods');
$faqs       = em_get_list_meta($post_id,'_em_faqs');
$related    = em_get_list_meta($post_id,'_em_related');
$alt_ids    = array_filter( array_map('intval', em_get_list_meta($post_id,'_em_alt_exercises')) );
$sources    = em_get_list_meta($post_id,'_em_sources');
$plans      = em_get_list_meta($post_id,'_em_workout_plans_list');
$calories   = get_post_meta($post_id,'_em_calories',true);
$last_updated = get_the_modified_date('F j, Y', $post_id);

$profile = [
    'Target Muscle' => get_post_meta($post_id,'_em_target_muscle',true),
    'Body Part'     => get_post_meta($post_id,'_em_body_part',true),
    'Equipment'     => get_post_meta($post_id,'_em_equipment',true),
    'Category'      => get_post_meta($post_id,'_em_category',true),
    'Skill Level'   => get_post_meta($post_id,'_em_skill_level',true),
    'Movement'      => get_post_meta($post_id,'_em_movement',true),
    'Also Known As' => get_post_meta($post_id,'_em_also_known_as',true),
];

$gif_media_id = (int) get_post_meta($post_id,'_em_gif_media_id',true);
$gif_meta     = $gif_media_id ? wp_get_attachment_metadata($gif_media_id) : [];
$final_gif    = ( $gif_media_id ? wp_get_attachment_url($gif_media_id) : '' ) ?: $gif_url;
$gif_w        = ! empty($gif_meta['width'])  ? (int) $gif_meta['width']  : 0;
$gif_h        = ! empty($gif_meta['height']) ? (int) $gif_meta['height'] : 0;
$muscle_map_id  = (int) get_post_meta($post_id,'_em_muscle_map_id',true);
$muscle_map_url = $muscle_map_id ? wp_get_attachment_url($muscle_map_id) : '';

// Mistakes/Tips are one text field until v2: "Title: description" is split at the first colon.
// Returns [title, body]. No split for long lead-ins or when the lead-in contains HTML/a URL.
if ( ! function_exists('em_split_lead') ) {
  function em_split_lead( $text ) {
    $pos = strpos( $text, ':' );
    if ( $pos === false || $pos > 90 ) return [ '', $text ];
    $lead = substr( $text, 0, $pos );
    if ( strpos( $lead, '<' ) !== false || preg_match( '/https?$/i', $lead ) ) return [ '', $text ];
    return [ trim( $lead ), trim( substr( $text, $pos + 1 ) ) ];
  }
}
// Muscle lines are "Name — what it does".
if ( ! function_exists('em_split_muscle') ) {
  function em_split_muscle( $line ) {
    $parts = preg_split( '/\s+[—–-]\s+/u', trim( $line ), 2 );
    return [ $parts[0], $parts[1] ?? '' ];
  }
}

// Keep only rows that will render, so headings and the contents menu never point at empty sections.
$steps    = array_values( array_filter( $steps, function($s){ return trim($s['title'] ?? '') !== '' || trim($s['desc'] ?? '') !== ''; } ) );
$sets_reps= array_values( array_filter( $sets_reps, function($r){ return ! empty($r['goal']); } ) );
$mistakes = array_values( array_filter( array_map('trim', $mistakes) ) );
$tips     = array_values( array_filter( array_map('trim', $tips) ) );
$mods     = array_values( array_filter( $mods, function($m){ return ! empty($m['title']); } ) );
$faqs     = array_values( array_filter( $faqs, function($f){ return ! empty($f['q']) && ! empty($f['a']); } ) );
$sources  = array_values( array_filter( $sources, function($s){ return ! empty($s['text']) || ! empty($s['url']); } ) );
$plans    = array_values( array_filter( $plans, function($p){ $id = (int) ($p['post_id'] ?? 0); return $id && get_post_status($id) === 'publish'; } ) );
$alt_ids  = array_values( array_filter( $alt_ids, function($id){ return get_post_status($id) === 'publish'; } ) );
$related_items = [];
foreach ( $related as $item ) {
    $rid = (int) ($item['post_id'] ?? 0);
    if ( $rid && get_post_status($rid) === 'publish' ) {
        $cats = get_post_type($rid) === 'post' ? get_the_category($rid) : [];
        $related_items[] = [ get_the_title($rid), get_permalink($rid), $cats ? $cats[0]->name : 'Guide' ];
    } elseif ( ! empty($item['title']) && ! empty($item['url']) ) {
        $url = strpos($item['url'], 'http') === 0 ? $item['url'] : home_url($item['url']);
        $related_items[] = [ $item['title'], $url, 'Guide' ];
    }
}

$toc = array_filter([
    'em-how-to'      => $steps     ? 'How to Do It'     : '',
    'em-muscles'     => ( $primary || $secondary ) ? 'Muscles Worked' : '',
    'em-sets'        => $sets_reps ? 'Sets & Reps'      : '',
    'em-mistakes'    => $mistakes  ? 'Common Mistakes'  : '',
    'em-tips'        => $tips      ? 'Tips'             : '',
    'em-mods'        => $mods      ? 'Modifications'    : '',
    'em-plans'       => $plans     ? 'Workout Plans'    : '',
    'em-alternatives'=> $alt_ids   ? 'Alternatives'     : '',
    'em-faq'         => $faqs      ? 'FAQs'             : '',
    'em-sources'     => $sources   ? 'Sources'          : '',
]);

get_header();
?>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap">
<style>
.em-page{--bg:#f8f7f5;--card:#fff;--subtle:#f0efed;--fg:#1a1917;--muted:#6b6860;--border:#e5e3de;--strong:#ccc9c2;
--accent:#c0392b;--accent-dark:#96291f;--accent-bg:#fdf1f0;--good:#1e7a4c;--good-bg:#eaf6ef}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .em-page{--bg:#141312;--card:#1e1d1b;--subtle:#252320;--fg:#f0ede8;--muted:#a8a49d;
--border:#2e2c28;--strong:#3d3a34;--accent:#e04d3d;--accent-dark:#f06050;--accent-bg:#2a1513;--good:#5cc28d;--good-bg:#14261c}}
:root[data-theme="dark"] .em-page{--bg:#141312;--card:#1e1d1b;--subtle:#252320;--fg:#f0ede8;--muted:#a8a49d;--border:#2e2c28;--strong:#3d3a34;
--accent:#e04d3d;--accent-dark:#f06050;--accent-bg:#2a1513;--good:#5cc28d;--good-bg:#14261c}
.em-page{background:var(--bg);color:var(--fg);font:16px/1.65 Inter,system-ui,-apple-system,"Segoe UI",Arial,sans-serif;padding-bottom:40px}
.em-page *{box-sizing:border-box}
.em-page a{color:var(--accent)}.em-page a:hover{color:var(--accent-dark)}
.em-page h1,.em-page h2,.em-page h3{font-family:inherit;color:var(--fg);text-transform:none}
.em-wrap{max-width:1080px;margin:0 auto;padding:0 16px}
.em-crumbs{font-size:13px;color:var(--muted);padding:18px 0 6px}
.em-crumbs a{color:var(--muted);text-decoration:none}
.em-page h1.em-h1{font-size:clamp(28px,4vw,40px);line-height:1.15;margin:4px 0 8px;letter-spacing:-.02em;font-weight:700}
.em-page h2{font-size:24px;line-height:1.25;margin:0 0 16px;letter-spacing:-.01em;font-weight:700}
.em-page h3{font-size:17px;line-height:1.35;margin:0 0 6px;font-weight:600}
.em-sub{color:var(--muted);font-size:17px;margin:0 0 14px;max-width:760px}
.em-chips{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 10px}
.em-chip{font-size:13px;padding:4px 12px;border-radius:999px;background:var(--subtle);border:1px solid var(--border);color:var(--fg)}
.em-updated{font-size:13px;color:var(--muted);margin:0 0 22px}
.em-hero{display:grid;grid-template-columns:1.25fr 1fr;gap:20px;margin-bottom:22px}
.em-card{background:var(--card);border:1px solid var(--border);border-radius:14px}
.em-gif{padding:12px;display:flex;align-items:center;justify-content:center}
.em-gif img{width:100%;max-width:440px;height:auto;border-radius:10px;background:#fff}
.em-profile{padding:18px 20px}.em-profile h2{font-size:18px;margin-bottom:10px}
.em-profile dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:9px 14px;font-size:14px}
.em-profile dt{color:var(--muted);margin:0}.em-profile dd{margin:0;font-weight:600}
.em-note{display:block;font-weight:400;font-size:12px;color:var(--muted)}
.em-qa{background:var(--accent-bg);border-left:4px solid var(--accent);border-radius:10px;padding:16px 20px;margin:0 0 22px}
.em-qa b{display:block;font-size:13px;text-transform:uppercase;letter-spacing:.06em;color:var(--accent);margin-bottom:4px}
.em-qa p{margin:0}
.em-layout{display:grid;grid-template-columns:220px 1fr;gap:28px;align-items:start}
.em-toc{position:sticky;top:16px;padding:16px;font-size:14px}.em-toc b{display:block;margin-bottom:8px}
.em-toc ol{margin:0;padding-left:18px}.em-toc li{margin:4px 0}
.em-toc a{color:var(--fg);text-decoration:none}.em-toc a:hover{color:var(--accent)}
.em-main{min-width:0}
.em-sec{padding:24px;margin-bottom:20px;scroll-margin-top:16px}
.em-steps{list-style:none;margin:0;padding:0}
.em-steps li{display:grid;grid-template-columns:36px 1fr;gap:14px;padding:12px 0;border-top:1px solid var(--border);margin:0}
.em-steps li:first-child{border-top:0}
.em-num{width:36px;height:36px;border-radius:50%;background:var(--accent);color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center}
.em-steps p,.em-item p{margin:0;color:var(--muted)}
.em-mus{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.em-mus.has-map{grid-template-columns:1fr 1fr 180px}
.em-mus h3{font-size:13px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);margin-bottom:8px}
.em-mus ul{list-style:none;margin:0;padding:0}.em-mus li{padding:8px 0;border-top:1px solid var(--border);font-size:15px;margin:0}
.em-mus li b{display:block}.em-mus li span{color:var(--muted);font-size:14px}
.em-mus img{width:100%;height:auto;border-radius:10px}
.em-tbl-wrap{overflow-x:auto}
.em-tbl{width:100%;border-collapse:collapse;font-size:15px;margin:0}
.em-tbl th,.em-tbl td{text-align:left;padding:10px 12px;border:0;border-bottom:1px solid var(--border)}
.em-tbl th{background:var(--subtle);font-size:13px;text-transform:uppercase;letter-spacing:.04em}
.em-item{display:grid;grid-template-columns:28px 1fr;gap:12px;padding:12px 0;border-top:1px solid var(--border)}
.em-item:first-of-type{border-top:0}
.em-ic{width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:14px}
.em-ic.x{background:var(--accent-bg);color:var(--accent)}.em-ic.ok{background:var(--good-bg);color:var(--good)}
.em-mods{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.em-mod{border:1px solid var(--border);border-radius:12px;padding:14px 16px;background:var(--bg)}
.em-lvl{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.05em}
.em-lvl.e{color:var(--good)}.em-lvl.h{color:var(--accent)}.em-mod p{margin:4px 0 0;color:var(--muted);font-size:15px}
.em-mod h3 a{color:var(--fg)}
.em-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.em-ccard{display:block;border:1px solid var(--border);border-radius:12px;padding:14px;background:var(--bg);color:var(--fg)!important;text-decoration:none!important}
.em-ccard:hover{border-color:var(--accent)}
.em-ccard img{width:100%;aspect-ratio:1/1;object-fit:contain;background:#fff;border-radius:8px;margin-bottom:8px}
.em-ccard small{color:var(--muted);display:block}
.em-plan{display:flex;gap:16px;align-items:center;border:1px solid var(--border);border-radius:12px;padding:16px;background:var(--bg);color:var(--fg)!important;text-decoration:none!important;margin-bottom:10px}
.em-plan:last-child{margin-bottom:0}.em-plan:hover{border-color:var(--accent)}
.em-day{background:var(--accent);color:#fff;border-radius:8px;padding:8px 12px;font-weight:700;font-size:14px;white-space:nowrap}
.em-faq details{border-top:1px solid var(--border);padding:12px 0}.em-faq details:first-of-type{border-top:0}
.em-faq summary{cursor:pointer;font-weight:600;list-style:none;display:flex;justify-content:space-between;gap:12px}
.em-faq summary::-webkit-details-marker{display:none}
.em-faq summary::after{content:"+";color:var(--accent);font-size:20px;line-height:1}
.em-faq details[open] summary::after{content:"\2212"}
.em-faq details p{margin:8px 0 0;color:var(--muted)}
.em-src{margin:0;padding-left:20px;font-size:14px;color:var(--muted)}.em-src li{margin-bottom:6px}.em-src a{word-break:break-word}
.em-disc{font-size:13px;color:var(--muted);padding:0 4px 20px;margin:0}
.em-cta{text-align:center;padding:26px}
.em-cta .em-sub{margin:0 auto 14px}
.em-btn{display:inline-block;background:var(--accent);color:#fff!important;text-decoration:none!important;padding:11px 22px;border-radius:999px;font-weight:600}
.em-btn:hover{background:var(--accent-dark)}
@media (max-width:860px){.em-hero,.em-layout,.em-mus,.em-mus.has-map,.em-mods{grid-template-columns:1fr}.em-toc{position:static}.em-cards{grid-template-columns:1fr 1fr}}
@media (max-width:520px){.em-cards{grid-template-columns:1fr}.em-sec{padding:18px}.em-plan{flex-direction:column;align-items:flex-start}}
</style>

<div class="em-page">
<div class="em-wrap">

  <nav class="em-crumbs" aria-label="Breadcrumb">
    <a href="<?php echo esc_url(home_url('/')); ?>">Home</a> ›
    <a href="<?php echo esc_url(home_url('/exercises/')); ?>">Exercises</a> ›
    <span><?php echo esc_html($title); ?></span>
  </nav>

  <h1 class="em-h1"><?php echo esc_html($title); ?></h1>
  <?php if ($subtitle): ?><p class="em-sub"><?php echo esc_html($subtitle); ?></p><?php endif; ?>
  <?php if ($tags): ?>
  <div class="em-chips"><?php foreach ($tags as $tag): ?><span class="em-chip"><?php echo esc_html($tag); ?></span><?php endforeach; ?></div>
  <?php endif; ?>
  <p class="em-updated">Last updated: <?php echo esc_html($last_updated); ?></p>

  <div class="em-hero">
    <?php if ($final_gif): ?>
    <div class="em-card em-gif">
      <img src="<?php echo esc_url($final_gif); ?>" alt="<?php echo esc_attr($gif_alt); ?>" loading="eager" fetchpriority="high" decoding="async"<?php if ($gif_w && $gif_h): ?> width="<?php echo (int) $gif_w; ?>" height="<?php echo (int) $gif_h; ?>"<?php endif; ?>>
    </div>
    <?php endif; ?>
    <div class="em-card em-profile">
      <h2>Exercise Profile</h2>
      <dl>
        <?php foreach ($profile as $label => $value): if (! $value) continue; ?>
        <dt><?php echo esc_html($label); ?></dt><dd><?php echo esc_html($value); ?></dd>
        <?php endforeach; ?>
        <?php if ($calories): ?>
        <dt>Est. Calories</dt><dd><?php echo esc_html($calories); ?> per set<span class="em-note">Estimate for a 70 kg person, 30–60 second set</span></dd>
        <?php endif; ?>
      </dl>
    </div>
  </div>

  <?php if ($qa): ?>
  <div class="em-qa" role="note"><b>Quick Answer</b><p><?php echo esc_html($qa); ?></p></div>
  <?php endif; ?>

  <div class="em-layout">
    <?php if ($toc): ?>
    <nav class="em-card em-toc" aria-label="Contents">
      <b>On this page</b>
      <ol><?php foreach ($toc as $id => $label): ?><li><a href="#<?php echo esc_attr($id); ?>"><?php echo esc_html($label); ?></a></li><?php endforeach; ?></ol>
    </nav>
    <?php endif; ?>

    <main class="em-main">

      <?php if ($steps): ?>
      <section id="em-how-to" class="em-card em-sec">
        <h2>How to Do the <?php echo esc_html($title); ?></h2>
        <ol class="em-steps">
          <?php foreach ($steps as $i => $step): $s_title = trim($step['title'] ?? ''); $s_desc = trim($step['desc'] ?? ''); ?>
          <li><span class="em-num"><?php echo (int) $i + 1; ?></span><div>
            <?php if ($s_title !== ''): ?><h3><?php echo esc_html($s_title); ?></h3><?php endif; ?>
            <?php if ($s_desc !== ''): ?><p><?php echo esc_html($s_desc); ?></p><?php endif; ?>
          </div></li>
          <?php endforeach; ?>
        </ol>
      </section>
      <?php endif; ?>

      <?php if ($primary || $secondary): ?>
      <section id="em-muscles" class="em-card em-sec">
        <h2>What Muscles Does the <?php echo esc_html($title); ?> Work?</h2>
        <div class="em-mus<?php echo $muscle_map_url ? ' has-map' : ''; ?>">
          <?php foreach ([ 'Primary' => $primary, 'Secondary' => $secondary ] as $group => $list): if (! $list) continue; ?>
          <div><h3><?php echo esc_html($group); ?></h3><ul>
            <?php foreach ($list as $line): if (trim($line) === '') continue; list($m_name, $m_desc) = em_split_muscle($line); ?>
            <li><b><?php echo esc_html($m_name); ?></b><?php if ($m_desc): ?><span><?php echo esc_html($m_desc); ?></span><?php endif; ?></li>
            <?php endforeach; ?>
          </ul></div>
          <?php endforeach; ?>
          <?php if ($muscle_map_url): ?>
          <div><img src="<?php echo esc_url($muscle_map_url); ?>" alt="<?php echo esc_attr($title); ?> muscles diagram" loading="lazy"></div>
          <?php endif; ?>
        </div>
      </section>
      <?php endif; ?>

      <?php if ($sets_reps): ?>
      <section id="em-sets" class="em-card em-sec">
        <h2>How Many Sets and Reps Should You Do?</h2>
        <div class="em-tbl-wrap"><table class="em-tbl">
          <thead><tr><th>Goal</th><th>Sets</th><th>Reps</th><th>Rest</th></tr></thead>
          <tbody><?php foreach ($sets_reps as $row): ?>
            <tr><td><b><?php echo esc_html($row['goal']); ?></b></td><td><?php echo esc_html($row['sets'] ?? ''); ?></td><td><?php echo esc_html($row['reps'] ?? ''); ?></td><td><?php echo esc_html($row['rest'] ?? ''); ?></td></tr>
          <?php endforeach; ?></tbody>
        </table></div>
      </section>
      <?php endif; ?>

      <?php if ($mistakes): ?>
      <section id="em-mistakes" class="em-card em-sec">
        <h2>Common Mistakes That Reduce Results</h2>
        <?php foreach ($mistakes as $mistake): list($m_title, $m_body) = em_split_lead(esc_html($mistake)); ?>
        <div class="em-item"><span class="em-ic x">✕</span><div>
          <?php if ($m_title): ?><h3><?php echo $m_title; ?></h3><?php endif; ?><p><?php echo $m_body; ?></p>
        </div></div>
        <?php endforeach; ?>
      </section>
      <?php endif; ?>

      <?php if ($tips): ?>
      <section id="em-tips" class="em-card em-sec">
        <h2>Tips for Better Results</h2>
        <?php foreach ($tips as $tip): list($t_title, $t_body) = em_split_lead(wp_kses_post($tip)); ?>
        <div class="em-item"><span class="em-ic ok">✓</span><div>
          <?php if ($t_title): ?><h3><?php echo $t_title; ?></h3><?php endif; ?><p><?php echo $t_body; ?></p>
        </div></div>
        <?php endforeach; ?>
      </section>
      <?php endif; ?>

      <?php if ($mods): ?>
      <section id="em-mods" class="em-card em-sec">
        <h2>Modifications and Progressions</h2>
        <div class="em-mods">
          <?php foreach ($mods as $mod):
            $harder  = ($mod['type'] ?? '') === 'harder';
            $link_id = (int) ($mod['link_id'] ?? 0);
            $link    = $link_id && get_post_status($link_id) === 'publish' ? get_permalink($link_id) : ''; ?>
          <div class="em-mod">
            <span class="em-lvl <?php echo $harder ? 'h' : 'e'; ?>"><?php echo $harder ? '▲ Harder' : '▼ Easier'; ?></span>
            <h3><?php echo $link ? '<a href="' . esc_url($link) . '">' . esc_html($mod['title']) . '</a>' : esc_html($mod['title']); ?></h3>
            <p><?php echo esc_html($mod['desc'] ?? ''); ?></p>
          </div>
          <?php endforeach; ?>
        </div>
      </section>
      <?php endif; ?>

      <?php if ($plans): ?>
      <section id="em-plans" class="em-card em-sec">
        <h2>Workout Plans With the <?php echo esc_html($title); ?></h2>
        <?php foreach ($plans as $plan): $pid = (int) $plan['post_id']; $day = trim($plan['day_label'] ?? ''); ?>
        <a class="em-plan" href="<?php echo esc_url(get_permalink($pid)); ?>">
          <span class="em-day"><?php echo esc_html($day !== '' ? $day : 'Plan'); ?></span>
          <b><?php echo esc_html(get_the_title($pid)); ?></b>
        </a>
        <?php endforeach; ?>
      </section>
      <?php endif; ?>

      <?php if ($alt_ids): ?>
      <section id="em-alternatives" class="em-card em-sec">
        <h2><?php echo esc_html($title); ?> Alternatives</h2>
        <div class="em-cards">
          <?php foreach ($alt_ids as $alt_id):
            $a_gif_id = (int) get_post_meta($alt_id,'_em_gif_media_id',true);
            $a_gif    = ( $a_gif_id ? wp_get_attachment_url($a_gif_id) : '' ) ?: get_post_meta($alt_id,'_em_gif_url',true);
            $a_target = get_post_meta($alt_id,'_em_target_muscle',true); ?>
          <a class="em-ccard" href="<?php echo esc_url(get_permalink($alt_id)); ?>">
            <?php if ($a_gif): ?><img src="<?php echo esc_url($a_gif); ?>" alt="<?php echo esc_attr(get_the_title($alt_id)); ?> exercise demonstration" loading="lazy" width="360" height="360"><?php endif; ?>
            <b><?php echo esc_html(get_the_title($alt_id)); ?></b>
            <?php if ($a_target): ?><small><?php echo esc_html($a_target); ?></small><?php endif; ?>
          </a>
          <?php endforeach; ?>
        </div>
      </section>
      <?php endif; ?>

      <?php if ($faqs): ?>
      <section id="em-faq" class="em-card em-sec em-faq">
        <h2>Frequently Asked Questions</h2>
        <?php foreach ($faqs as $faq): ?>
        <details><summary><?php echo esc_html($faq['q']); ?></summary><p><?php echo esc_html($faq['a']); ?></p></details>
        <?php endforeach; ?>
      </section>
      <?php endif; ?>

      <?php if ($sources): ?>
      <section id="em-sources" class="em-card em-sec">
        <h2>Sources</h2>
        <ol class="em-src">
          <?php foreach ($sources as $src): $s_text = $src['text'] ?? ''; $s_url = $src['url'] ?? ''; ?>
          <li><?php echo esc_html($s_text); ?><?php if ($s_url): ?> <a href="<?php echo esc_url($s_url); ?>" target="_blank" rel="noopener"><?php echo esc_html($s_url); ?></a><?php endif; ?></li>
          <?php endforeach; ?>
        </ol>
      </section>
      <?php endif; ?>

      <?php if ($related_items): ?>
      <section class="em-card em-sec">
        <h2>Related Training Articles</h2>
        <div class="em-cards">
          <?php foreach ($related_items as $r): ?>
          <a class="em-ccard" href="<?php echo esc_url($r[1]); ?>"><small><?php echo esc_html($r[2]); ?></small><b><?php echo esc_html($r[0]); ?></b></a>
          <?php endforeach; ?>
        </div>
      </section>
      <?php endif; ?>

      <p class="em-disc">If you have an existing injury or medical condition, check with your doctor before adding this exercise to your training.</p>

      <div class="em-card em-cta">
        <h2>Looking for more exercises?</h2>
        <p class="em-sub">Browse the full exercise library.</p>
        <a class="em-btn" href="<?php echo esc_url(home_url('/exercises/')); ?>">Browse All Exercises →</a>
      </div>

    </main>
  </div>

</div>
</div>

<?php get_footer(); ?>
