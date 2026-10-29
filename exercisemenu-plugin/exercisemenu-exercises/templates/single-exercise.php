<?php
/**
 * Single Exercise Template
 * ExerciseMenu — all styling matches the approved HTML design
 */
if ( ! defined('ABSPATH') ) exit;

$post_id    = get_the_ID();
$title      = get_the_title();
$subtitle   = get_post_meta($post_id,'_em_subtitle',true);
$tags_raw   = get_post_meta($post_id,'_em_tags',true);
$tags       = $tags_raw ? array_filter(array_map('trim', explode(',', $tags_raw))) : [];
$gif_url    = get_post_meta($post_id,'_em_gif_url',true);
$gif_alt    = get_post_meta($post_id,'_em_gif_alt',true) ?: $title . ' exercise animation — proper form demonstration';
$qa         = get_post_meta($post_id,'_em_quick_answer',true);
$primary = em_get_list_meta($post_id,'_em_primary_muscles');
$secondary = em_get_list_meta($post_id,'_em_secondary_muscles');
$steps = em_get_list_meta($post_id,'_em_steps');
$sets_reps = em_get_list_meta($post_id,'_em_sets_reps');
$mistakes = em_get_list_meta($post_id,'_em_mistakes');
$tips = em_get_list_meta($post_id,'_em_tips');
$mods = em_get_list_meta($post_id,'_em_mods');
$faqs = em_get_list_meta($post_id,'_em_faqs');
$related = em_get_list_meta($post_id,'_em_related');
$target_m   = get_post_meta($post_id,'_em_target_muscle',true);
$body_part  = get_post_meta($post_id,'_em_body_part',true);
$equipment  = get_post_meta($post_id,'_em_equipment',true);
$category   = get_post_meta($post_id,'_em_category',true);
$skill      = get_post_meta($post_id,'_em_skill_level',true);
$movement   = get_post_meta($post_id,'_em_movement',true);
$aka        = get_post_meta($post_id,'_em_also_known_as',true);
$calories   = get_post_meta($post_id,'_em_calories',true);

// v1.1 new fields
$gif_media_id    = (int) get_post_meta($post_id,'_em_gif_media_id',true);
$gif_media_url   = $gif_media_id ? wp_get_attachment_url($gif_media_id) : '';
$gif_media_meta  = $gif_media_id ? wp_get_attachment_metadata($gif_media_id) : [];
$gif_width       = ! empty($gif_media_meta['width'])  ? (int) $gif_media_meta['width']  : 0;
$gif_height      = ! empty($gif_media_meta['height']) ? (int) $gif_media_meta['height'] : 0;
$final_gif       = $gif_media_url ?: $gif_url;

$muscle_map_id   = (int) get_post_meta($post_id,'_em_muscle_map_id',true);
$muscle_map_url  = $muscle_map_id ? wp_get_attachment_url($muscle_map_id) : '';

$alt_exercises   = em_get_list_meta($post_id,'_em_alt_exercises');
$sources         = em_get_list_meta($post_id,'_em_sources');
$workout_plans_list = em_get_list_meta($post_id,'_em_workout_plans_list');

// Mistakes/Tips are single text fields until v2. Bold the lead-in before the first colon
// ("Flaring the Elbows: Letting…"). Skips colons inside HTML or URLs and long lead-ins.
if ( ! function_exists('em_bold_lead') ) {
  function em_bold_lead( $html ) {
    $pos = strpos( $html, ':' );
    if ( $pos === false || $pos > 90 ) return $html;
    $lead = substr( $html, 0, $pos );
    if ( strpos( $lead, '<' ) !== false || preg_match( '/https?$/i', $lead ) ) return $html;
    return '<strong>' . $lead . ':</strong>' . substr( $html, $pos + 1 );
  }
}

$last_updated    = get_the_modified_date('F j, Y', $post_id);

get_header();
?>
<style>
:root {
  --bg:#f8f7f5;--bg-card:#ffffff;--bg-subtle:#f0efed;--fg:#1a1917;
  --fg-muted:#6b6860;--fg-xmuted:#9e9b95;--accent:#c0392b;--accent-dark:#96291f;
  --accent-bg:#fdf1f0;--border:#e5e3de;--border-strong:#ccc9c2;--tag-bg:#eceae6;
  --font-display:'Barlow Condensed',system-ui,sans-serif;
  --font-body:'Inter',system-ui,sans-serif;
  --radius-sm:4px;--radius-md:8px;--radius-lg:12px;
  color-scheme:light;
}
@media(prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --bg:#141312;--bg-card:#1e1d1b;--bg-subtle:#252320;--fg:#f0ede8;
    --fg-muted:#a8a49d;--fg-xmuted:#6e6a63;--accent:#e04d3d;--accent-dark:#f06050;
    --accent-bg:#2a1513;--border:#2e2c28;--border-strong:#3d3a34;--tag-bg:#2a2925;
    color-scheme:dark;
  }
}
:root[data-theme="dark"]{
  --bg:#141312;--bg-card:#1e1d1b;--bg-subtle:#252320;--fg:#f0ede8;
  --fg-muted:#a8a49d;--fg-xmuted:#6e6a63;--accent:#e04d3d;--accent-dark:#f06050;
  --accent-bg:#2a1513;--border:#2e2c28;--border-strong:#3d3a34;--tag-bg:#2a2925;
  color-scheme:dark;
}
.em-page{font-family:var(--font-body);font-size:16px;line-height:1.65;color:var(--fg);background:var(--bg);}
.em-page a{color:var(--accent);text-decoration:none;}
.em-page a:hover{text-decoration:underline;color:var(--accent-dark);}
.em-page img{max-width:100%;display:block;}

.em-breadcrumb{background:var(--bg-subtle);border-bottom:1px solid var(--border);padding:10px 16px;}
.em-breadcrumb ol{display:flex;flex-wrap:wrap;gap:6px;align-items:center;list-style:none;margin:0;padding:0;font-size:13px;color:var(--fg-muted);}
.em-breadcrumb li+li::before{content:"›";margin-right:6px;color:var(--fg-xmuted);}
.em-breadcrumb a{color:var(--fg-muted);}
.em-breadcrumb li:last-child{color:var(--fg);font-weight:500;}

.em-layout{max-width:1160px;margin:0 auto;display:grid;grid-template-columns:1fr 300px;gap:40px;align-items:start;padding:40px 16px;}
@media(max-width:860px){.em-layout{grid-template-columns:1fr;padding:24px 16px;gap:32px;}}
.em-main{min-width:0;}
.em-sidebar{min-width:0;}
@media(min-width:861px){.em-sidebar{position:sticky;top:80px;}}

.em-hero{background:var(--bg-subtle);border:1px solid var(--border);border-radius:var(--radius-lg);overflow:hidden;margin-bottom:32px;aspect-ratio:1/1;display:flex;align-items:center;justify-content:center;max-width:720px;}
.em-hero img{width:100%;height:100%;object-fit:cover;}

.em-title-block{margin-bottom:24px;}
.em-h1{font-family:var(--font-display);font-size:clamp(32px,5vw,48px);font-weight:700;line-height:1.1;text-wrap:balance;color:var(--fg);margin:0 0 12px;letter-spacing:.5px;}
.em-subtitle{font-size:17px;color:var(--fg-muted);margin:0;line-height:1.5;}
.em-tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px;}
.em-tag{font-size:12px;font-weight:600;letter-spacing:.3px;padding:4px 10px;border-radius:20px;background:var(--tag-bg);color:var(--fg-muted);border:1px solid var(--border);}
.em-tag.accent{background:var(--accent-bg);color:var(--accent);border-color:transparent;}

.em-qa{background:var(--accent-bg);border-left:3px solid var(--accent);border-radius:0 var(--radius-md) var(--radius-md) 0;padding:16px 20px;margin-bottom:32px;}
.em-qa-label{font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:var(--accent);margin-bottom:6px;}
.em-qa p{margin:0;font-size:15px;line-height:1.55;color:var(--fg);}

.em-section{margin-bottom:36px;}
.em-section h2{font-family:var(--font-display);font-size:clamp(20px,3vw,26px);font-weight:700;letter-spacing:.3px;color:var(--fg);margin:0 0 16px;text-wrap:balance;padding-bottom:10px;border-bottom:2px solid var(--border);}
.em-section h3{font-size:16px;font-weight:600;color:var(--fg);margin:24px 0 10px;}
.em-section p{font-size:15px;line-height:1.7;color:var(--fg);margin:0 0 14px;}

.em-steps{list-style:none;margin:0;padding:0;counter-reset:steps;display:flex;flex-direction:column;gap:16px;}
.em-steps li{display:flex;gap:16px;align-items:flex-start;}
.em-step-num{flex-shrink:0;width:32px;height:32px;border-radius:50%;background:var(--accent);color:#fff;font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center;}
.em-step-content strong{display:block;font-size:15px;font-weight:600;color:var(--fg);margin-bottom:4px;}
.em-step-content span{font-size:14px;color:var(--fg-muted);line-height:1.55;}

.em-info-list{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:12px;}
.em-info-list li{display:flex;gap:12px;font-size:15px;line-height:1.6;align-items:flex-start;}
.em-icon{flex-shrink:0;width:20px;height:20px;margin-top:2px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;}
.em-info-list.mistakes .em-icon{background:var(--accent-bg);color:var(--accent);border:1px solid var(--accent);}
.em-info-list.tips .em-icon{background:#eef8f2;color:#1a7a4a;border:1px solid #b8dfc9;}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]) .em-info-list.tips .em-icon{background:#14261c;color:#5cc28d;border-color:#2d5a40;}}
:root[data-theme="dark"] .em-info-list.tips .em-icon{background:#14261c;color:#5cc28d;border-color:#2d5a40;}

.em-muscle-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:12px;margin-top:8px;}
.em-muscle-card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-md);padding:12px 14px;}
.em-muscle-card .label{font-size:11px;font-weight:600;letter-spacing:.6px;text-transform:uppercase;color:var(--fg-xmuted);margin-bottom:4px;}
.em-muscle-card .name{font-size:14px;font-weight:600;color:var(--fg);}
.em-muscle-card.primary{border-left:3px solid var(--accent);}
.em-muscle-card.secondary{border-left:3px solid var(--border-strong);}

.em-sets-wrap{overflow-x:auto;}
.em-sets-table{width:100%;border-collapse:collapse;font-size:14px;}
.em-sets-table th{background:var(--bg-subtle);padding:10px 14px;text-align:left;font-weight:600;color:var(--fg-muted);font-size:12px;letter-spacing:.4px;text-transform:uppercase;border-bottom:2px solid var(--border);}
.em-sets-table td{padding:11px 14px;border-bottom:1px solid var(--border);color:var(--fg);}
.em-sets-table tr:last-child td{border-bottom:none;}
.em-sets-table tr:hover td{background:var(--bg-subtle);}
.em-sets-table .goal{font-weight:600;}

.em-mods-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;}
@media(max-width:560px){.em-mods-grid{grid-template-columns:1fr;}}
.em-mod-card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-md);padding:16px;}
.em-mod-card h3{font-size:14px;font-weight:700;margin:0 0 8px;color:var(--fg);}
.em-mod-card p{font-size:13px;color:var(--fg-muted);margin:0;line-height:1.5;}

.em-link-list{display:flex;flex-direction:column;gap:10px;}
.em-link-card{display:flex;align-items:center;justify-content:space-between;gap:12px;background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-md);padding:14px 16px;color:var(--fg);transition:border-color .15s,background .15s;}
.em-link-card:hover{border-color:var(--accent);background:var(--accent-bg);text-decoration:none;}
.em-link-card strong{display:block;font-size:14px;font-weight:600;color:var(--fg);}
.em-link-card span{font-size:12px;color:var(--fg-muted);}
.em-link-card-arrow{color:var(--fg-xmuted);font-size:18px;flex-shrink:0;}

.em-faq-list{border:1px solid var(--border);border-radius:var(--radius-lg);overflow:hidden;}
.em-faq-item{border-bottom:1px solid var(--border);}
.em-faq-item:last-child{border-bottom:none;}
.em-faq-q{display:flex;align-items:center;justify-content:space-between;gap:12px;width:100%;background:var(--bg-card);border:none;cursor:pointer;text-align:left;padding:16px 20px;font-family:var(--font-body);font-size:15px;font-weight:600;color:var(--fg);transition:background .15s;}
.em-faq-q:hover{background:var(--bg-subtle);}
.em-faq-q[aria-expanded="true"]{color:var(--accent);}
.em-faq-icon{flex-shrink:0;width:20px;height:20px;border-radius:50%;border:1px solid var(--border);display:flex;align-items:center;justify-content:center;font-size:14px;color:var(--fg-muted);transition:transform .2s;}
.em-faq-q[aria-expanded="true"] .em-faq-icon{transform:rotate(45deg);border-color:var(--accent);color:var(--accent);}
.em-faq-a{max-height:0;overflow:hidden;transition:max-height .25s ease;}
.em-faq-a-inner{padding:0 20px 16px;font-size:14px;line-height:1.65;color:var(--fg-muted);background:var(--bg-card);}

.em-sidebar-card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);overflow:hidden;margin-bottom:20px;}
.em-sidebar-card-header{padding:14px 16px;background:var(--bg-subtle);border-bottom:1px solid var(--border);font-size:12px;font-weight:700;letter-spacing:.8px;text-transform:uppercase;color:var(--fg-muted);}
.em-profile-row{display:flex;justify-content:space-between;align-items:center;padding:11px 16px;border-bottom:1px solid var(--border);gap:8px;}
.em-profile-row:last-child{border-bottom:none;}
.em-profile-label{font-size:13px;color:var(--fg-muted);flex-shrink:0;}
.em-profile-value{font-size:13px;font-weight:600;color:var(--fg);text-align:right;}
.em-badge{display:inline-block;font-size:11px;font-weight:700;padding:3px 8px;border-radius:12px;letter-spacing:.3px;}
.em-badge.beginner{background:#e8f5ee;color:#1a6e3a;}
.em-badge.intermediate{background:#fef3cd;color:#7a5c00;}
.em-badge.advanced{background:#fde8e8;color:#8b0000;}
.em-calorie-pill{display:flex;align-items:center;gap:8px;background:var(--accent-bg);border:1px solid var(--accent);border-radius:var(--radius-md);padding:10px 14px;margin:12px 16px 16px;font-size:13px;color:var(--accent);}
.em-plan-list{list-style:none;margin:0;padding:0;}
.em-plan-item a{display:flex;align-items:center;gap:10px;padding:12px 16px;border-bottom:1px solid var(--border);color:var(--fg);text-decoration:none;font-size:13px;font-weight:500;transition:background .15s;}
.em-plan-item:last-child a{border-bottom:none;}
.em-plan-item a:hover{background:var(--accent-bg);color:var(--accent);}
.em-plan-dot{width:6px;height:6px;border-radius:50%;background:var(--accent);flex-shrink:0;}
.em-plan-meta{font-size:11px;color:var(--fg-xmuted);font-weight:400;display:block;}
.em-coming-soon{display:flex;align-items:center;gap:10px;padding:12px 16px;border-bottom:1px solid var(--border);font-size:13px;font-weight:500;color:var(--fg-muted);opacity:.6;}

.em-divider{border:none;border-top:1px solid var(--border);margin:32px 0;}
.em-back{display:inline-flex;align-items:center;gap:6px;font-size:14px;font-weight:500;color:var(--fg-muted);padding:8px 0;text-decoration:none;margin-bottom:32px;}
.em-back:hover{color:var(--accent);text-decoration:none;}

.em-cta-browse{background:var(--accent-bg);border:1px solid var(--accent);border-radius:var(--radius-lg);text-align:center;padding:36px 24px;margin-top:40px;}
.em-cta-browse-heading{font-family:var(--font-display);font-size:22px;font-weight:700;color:var(--fg);margin:0 0 8px;}
.em-cta-browse-sub{font-size:15px;color:var(--fg-muted);margin:0 0 24px;}
.em-cta-browse-btn{display:inline-block;background:var(--accent);color:#ffffff !important;font-size:15px;font-weight:600;padding:13px 28px;border-radius:var(--radius-md);text-decoration:none !important;transition:background .15s;}
.em-cta-browse-btn:hover{background:var(--accent-dark);color:#ffffff !important;text-decoration:none !important;}

.em-last-updated{font-size:12px;color:var(--fg-xmuted);margin:6px 0 0;}
.em-calorie-note{font-size:11px;color:var(--fg-xmuted);margin:-8px 16px 14px;line-height:1.4;}
.em-plan-day{font-size:12px;color:var(--fg-muted);margin-top:2px;}
.em-alt-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:16px;}
.em-alt-card{display:block;border:1px solid var(--border);border-radius:var(--radius-md);overflow:hidden;color:var(--fg);background:var(--bg-card);transition:border-color .15s;}
.em-alt-card:hover{border-color:var(--accent);text-decoration:none;}
.em-alt-card-img{aspect-ratio:1/1;background:#fff;overflow:hidden;}
.em-alt-card-img img{width:100%;height:100%;object-fit:contain;}
.em-alt-card-title{padding:12px 14px;font-size:14px;font-weight:600;color:var(--fg);}
.em-sources-list{padding-left:20px;font-size:14px;color:var(--fg-muted);margin:0;}
.em-sources-list li{margin-bottom:6px;}
.em-muscles-wrap{display:flex;gap:24px;align-items:flex-start;flex-wrap:wrap;}
.em-muscles-wrap .em-muscle-grid{flex:1;min-width:260px;}
.em-muscle-map{flex:0 0 180px;max-width:180px;}
.em-muscle-map img{width:100%;height:auto;border-radius:var(--radius-md);}
</style>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Barlow+Condensed:wght@600;700&display=swap">

<div class="em-page">

  <nav class="em-breadcrumb" aria-label="Breadcrumb">
    <ol>
      <li><a href="<?php echo esc_url(home_url('/')); ?>">Home</a></li>
      <li><a href="<?php echo esc_url(home_url('/exercises/')); ?>">Exercises</a></li>
      <li><?php echo esc_html($title); ?></li>
    </ol>
  </nav>

  <div class="em-layout">
    <main class="em-main">

      <a href="<?php echo esc_url(home_url('/exercises/')); ?>" class="em-back">← All exercises</a>

      <div class="em-title-block">
        <h1 class="em-h1"><?php echo esc_html($title); ?></h1>
        <?php if ($subtitle): ?>
        <p class="em-subtitle"><?php echo esc_html($subtitle); ?></p>
        <?php endif; ?>
        <p class="em-last-updated">Last updated: <?php echo esc_html($last_updated); ?></p>
        <?php if (!empty($tags)): ?>
        <div class="em-tags">
          <?php foreach ($tags as $i => $tag): ?>
          <span class="em-tag<?php echo $i === 0 ? ' accent' : ''; ?>"><?php echo esc_html(trim($tag)); ?></span>
          <?php endforeach; ?>
        </div>
        <?php endif; ?>
      </div>

      <?php if ($final_gif): ?>
      <div class="em-hero">
        <img src="<?php echo esc_url($final_gif); ?>" alt="<?php echo esc_attr($gif_alt); ?>" loading="eager" fetchpriority="high" decoding="async"<?php if ($gif_width && $gif_height): ?> width="<?php echo $gif_width; ?>" height="<?php echo $gif_height; ?>"<?php endif; ?>>
      </div>
      <?php endif; ?>

      <?php if ($qa): ?>
      <div class="em-qa" role="note">
        <div class="em-qa-label">Quick Answer</div>
        <p><?php echo esc_html($qa); ?></p>
      </div>
      <?php endif; ?>

      <?php if (!empty($steps)): ?>
      <div class="em-section">
        <h2>How to Do the <?php echo esc_html($title); ?></h2>
        <ol class="em-steps">
          <?php $step_no = 0; foreach ($steps as $step):
            $s_title = trim($step['title'] ?? '');
            $s_desc  = trim($step['desc'] ?? '');
            if ($s_title === '' && $s_desc === '') continue;
            $step_no++; ?>
          <li>
            <div class="em-step-num"><?php echo (int) $step_no; ?></div>
            <div class="em-step-content">
              <?php if ($s_title !== ''): ?><strong><?php echo esc_html($s_title); ?></strong><?php endif; ?>
              <?php if ($s_desc !== ''): ?><span><?php echo esc_html($s_desc); ?></span><?php endif; ?>
            </div>
          </li>
          <?php endforeach; ?>
        </ol>
      </div>
      <hr class="em-divider">
      <?php endif; ?>

      <?php if (!empty($primary) || !empty($secondary)): ?>
      <div class="em-section">
        <h2>What Muscles Does the <?php echo esc_html($title); ?> Work?</h2>
        <div class="em-muscles-wrap">
          <div class="em-muscle-grid">
            <?php foreach ($primary as $m): ?>
            <?php if (empty(trim($m))) continue; ?>
            <div class="em-muscle-card primary">
              <div class="label">Primary</div>
              <div class="name"><?php echo esc_html(trim($m)); ?></div>
            </div>
            <?php endforeach; ?>
            <?php foreach ($secondary as $m): ?>
            <?php if (empty(trim($m))) continue; ?>
            <div class="em-muscle-card secondary">
              <div class="label">Secondary</div>
              <div class="name"><?php echo esc_html(trim($m)); ?></div>
            </div>
            <?php endforeach; ?>
          </div>
          <?php if ($muscle_map_url): ?>
          <div class="em-muscle-map">
            <img src="<?php echo esc_url($muscle_map_url); ?>" alt="<?php echo esc_attr($title); ?> muscles diagram" loading="lazy">
          </div>
          <?php endif; ?>
        </div>
      </div>
      <hr class="em-divider">
      <?php endif; ?>

      <?php if (!empty($sets_reps)): ?>
      <div class="em-section">
        <h2>How Many Sets and Reps Should You Do?</h2>
        <div class="em-sets-wrap">
          <table class="em-sets-table">
            <thead><tr><th>Goal</th><th>Sets</th><th>Reps</th><th>Rest</th></tr></thead>
            <tbody>
              <?php foreach ($sets_reps as $row): ?>
              <?php if (empty($row['goal'])) continue; ?>
              <tr>
                <td class="goal"><?php echo esc_html($row['goal']); ?></td>
                <td><?php echo esc_html($row['sets'] ?? ''); ?></td>
                <td><?php echo esc_html($row['reps'] ?? ''); ?></td>
                <td><?php echo esc_html($row['rest'] ?? ''); ?></td>
              </tr>
              <?php endforeach; ?>
            </tbody>
          </table>
        </div>
      </div>
      <hr class="em-divider">
      <?php endif; ?>

      <?php if (!empty($mistakes)): ?>
      <div class="em-section">
        <h2>Common Mistakes That Reduce Results</h2>
        <ul class="em-info-list mistakes">
          <?php foreach ($mistakes as $mistake): ?>
          <?php if (empty(trim($mistake))) continue; ?>
          <li><div class="em-icon">✕</div><div><?php echo em_bold_lead(esc_html(trim($mistake))); ?></div></li>
          <?php endforeach; ?>
        </ul>
      </div>
      <hr class="em-divider">
      <?php endif; ?>

      <?php if (!empty($tips)): ?>
      <div class="em-section">
        <h2>Tips for Better Results</h2>
        <ul class="em-info-list tips">
          <?php foreach ($tips as $tip): ?>
          <?php if (empty(trim($tip))) continue; ?>
          <li><div class="em-icon">✓</div><div><?php echo em_bold_lead(wp_kses_post(trim($tip))); ?></div></li>
          <?php endforeach; ?>
        </ul>
      </div>
      <hr class="em-divider">
      <?php endif; ?>

      <?php if (!empty($mods)): ?>
      <div class="em-section">
        <h2>Modifications and Progressions</h2>
        <div class="em-mods-grid">
          <?php foreach ($mods as $mod): ?>
          <?php if (empty($mod['title'])) continue; ?>
          <?php
            $mod_link_id = (int) ($mod['link_id'] ?? 0);
            $mod_link    = $mod_link_id ? get_permalink($mod_link_id) : '';
            $mod_title_html = $mod_link
              ? '<a href="' . esc_url($mod_link) . '">' . esc_html($mod['title']) . '</a>'
              : esc_html($mod['title']);
          ?>
          <div class="em-mod-card">
            <?php $is_harder = ($mod['type'] ?? '') === 'harder'; ?>
            <h3><?php echo $is_harder ? '🔼 Harder' : '🔽 Easier'; ?> — <?php echo $mod_title_html; ?></h3>
            <p><?php echo esc_html($mod['desc'] ?? ''); ?></p>
          </div>
          <?php endforeach; ?>
        </div>
      </div>
      <hr class="em-divider">
      <?php endif; ?>

      <?php // ─── Workout Plans Using This Exercise (v1.1) ─── ?>
      <?php if (!empty($workout_plans_list)): ?>
      <div class="em-section">
        <h2>Workout Plans With <?php echo esc_html($title); ?></h2>
        <div class="em-link-list">
          <?php foreach ($workout_plans_list as $wp_plan): ?>
            <?php
              $wp_id = (int) ($wp_plan['post_id'] ?? 0);
              if ( ! $wp_id || get_post_status($wp_id) !== 'publish' ) continue;
              $wp_title = get_the_title($wp_id);
              $wp_link  = get_permalink($wp_id);
              $wp_day   = $wp_plan['day_label'] ?? '';
            ?>
            <a class="em-link-card" href="<?php echo esc_url($wp_link); ?>">
              <div>
                <strong><?php echo esc_html($wp_title); ?></strong>
                <?php if ($wp_day): ?><div class="em-plan-day"><?php echo esc_html($wp_day); ?></div><?php endif; ?>
              </div>
              <div class="em-link-card-arrow">›</div>
            </a>
          <?php endforeach; ?>
        </div>
      </div>
      <hr class="em-divider">
      <?php endif; ?>

      <?php // ─── Alternative Exercises (v1.1) ─── ?>
      <?php
        $alt_ids = array_filter( array_map('intval', (array) $alt_exercises) );
        if ( ! empty($alt_ids) ):
      ?>
      <div class="em-section">
        <h2><?php echo esc_html($title); ?> Alternatives</h2>
        <div class="em-alt-grid">
          <?php foreach ($alt_ids as $alt_id): ?>
            <?php
              $alt_post = get_post($alt_id);
              if ( ! $alt_post || $alt_post->post_status !== 'publish' ) continue;
              $alt_gif_id  = (int) get_post_meta($alt_id,'_em_gif_media_id',true);
              $alt_gif_url = $alt_gif_id ? wp_get_attachment_url($alt_gif_id) : get_post_meta($alt_id,'_em_gif_url',true);
            ?>
            <a href="<?php echo esc_url(get_permalink($alt_id)); ?>" class="em-alt-card">
              <?php if ($alt_gif_url): ?>
                <div class="em-alt-card-img">
                  <img src="<?php echo esc_url($alt_gif_url); ?>" alt="<?php echo esc_attr(get_the_title($alt_id)); ?> exercise demonstration" loading="lazy" width="360" height="360">
                </div>
              <?php endif; ?>
              <div class="em-alt-card-title"><?php echo esc_html(get_the_title($alt_id)); ?></div>
            </a>
          <?php endforeach; ?>
        </div>
      </div>
      <hr class="em-divider">
      <?php endif; ?>

      <?php if (!empty($related)): ?>
      <div class="em-section">
        <h2>Related Training Articles</h2>
        <div class="em-link-list">
          <?php foreach ($related as $item):
            // v1.1 priority: use post_id if set; else legacy text url
            $rel_post_id = (int) ($item['post_id'] ?? 0);
            $rel_title   = '';
            $rel_url     = '';
            if ( $rel_post_id && get_post_status($rel_post_id) === 'publish' ) {
              $rel_title = get_the_title($rel_post_id);
              $rel_url   = get_permalink($rel_post_id);
            } elseif ( ! empty($item['title']) && ! empty($item['url']) ) {
              $rel_title = $item['title'];
              $rel_url   = ( strpos($item['url'], 'http') === 0 ) ? $item['url'] : home_url($item['url']);
            } else {
              continue;
            }
          ?>
          <a class="em-link-card" href="<?php echo esc_url($rel_url); ?>">
            <div><strong><?php echo esc_html($rel_title); ?></strong></div>
            <div class="em-link-card-arrow">›</div>
          </a>
          <?php endforeach; ?>
        </div>
      </div>
      <hr class="em-divider">
      <?php endif; ?>

      <?php // ─── Sources (v1.1) ─── ?>
      <?php if (!empty($sources)): ?>
      <div class="em-section em-sources">
        <h2>Sources</h2>
        <ol class="em-sources-list">
          <?php foreach ($sources as $src): ?>
            <?php
              $s_text = $src['text'] ?? '';
              $s_url  = $src['url']  ?? '';
              if ( ! $s_text && ! $s_url ) continue;
            ?>
            <li>
              <?php if ($s_url): ?>
                <a href="<?php echo esc_url($s_url); ?>" target="_blank" rel="noopener"><?php echo esc_html($s_text ?: $s_url); ?></a>
              <?php else: ?>
                <?php echo esc_html($s_text); ?>
              <?php endif; ?>
            </li>
          <?php endforeach; ?>
        </ol>
      </div>
      <hr class="em-divider">
      <?php endif; ?>

      <?php if (!empty($faqs)): ?>
      <div class="em-section">
        <h2>Frequently Asked Questions</h2>
        <div class="em-faq-list" id="em-faq">
          <?php foreach ($faqs as $i => $faq): ?>
          <?php if (empty($faq['q']) || empty($faq['a'])) continue; ?>
          <div class="em-faq-item">
            <button class="em-faq-q" aria-expanded="false" aria-controls="em-faq-<?php echo $i; ?>">
              <?php echo esc_html($faq['q']); ?>
              <span class="em-faq-icon">+</span>
            </button>
            <div class="em-faq-a" id="em-faq-<?php echo $i; ?>" role="region">
              <div class="em-faq-a-inner">
                <p><?php echo esc_html($faq['a']); ?></p>
              </div>
            </div>
          </div>
          <?php endforeach; ?>
        </div>
      </div>
      <?php endif; ?>

      <div class="em-cta-browse">
        <p class="em-cta-browse-heading">Looking for more exercises?</p>
        <p class="em-cta-browse-sub">Browse the full exercise library.</p>
        <a href="<?php echo esc_url(home_url('/exercises/')); ?>" class="em-cta-browse-btn">Browse All Exercises →</a>
      </div>

    </main>

    <aside class="em-sidebar">

      <div class="em-sidebar-card">
        <div class="em-sidebar-card-header">Exercise Profile</div>
        <?php if ($target_m): ?><div class="em-profile-row"><span class="em-profile-label">Target Muscle</span><span class="em-profile-value"><?php echo esc_html($target_m); ?></span></div><?php endif; ?>
        <?php if ($body_part): ?><div class="em-profile-row"><span class="em-profile-label">Body Part</span><span class="em-profile-value"><?php echo esc_html($body_part); ?></span></div><?php endif; ?>
        <?php if ($equipment): ?><div class="em-profile-row"><span class="em-profile-label">Equipment</span><span class="em-profile-value"><?php echo esc_html($equipment); ?></span></div><?php endif; ?>
        <?php if ($category): ?><div class="em-profile-row"><span class="em-profile-label">Category</span><span class="em-profile-value"><?php echo esc_html($category); ?></span></div><?php endif; ?>
        <?php if ($skill): ?>
        <div class="em-profile-row">
          <span class="em-profile-label">Skill Level</span>
          <span class="em-profile-value"><span class="em-badge <?php echo esc_attr(strtolower($skill)); ?>"><?php echo esc_html($skill); ?></span></span>
        </div>
        <?php endif; ?>
        <?php if ($movement): ?><div class="em-profile-row"><span class="em-profile-label">Movement Pattern</span><span class="em-profile-value"><?php echo esc_html($movement); ?></span></div><?php endif; ?>
        <?php if ($aka): ?><div class="em-profile-row"><span class="em-profile-label">Also Known As</span><span class="em-profile-value" style="font-size:12px"><?php echo esc_html($aka); ?></span></div><?php endif; ?>
        <?php if ($calories): ?>
        <div class="em-calorie-pill">
          <span>Est. <strong><?php echo esc_html($calories); ?></strong> per set</span>
        </div>
        <p class="em-calorie-note">Estimate for a 70 kg person, 30–60 second set.</p>
        <?php endif; ?>
      </div>

    </aside>
  </div>

</div>

<script>
(function(){
  document.querySelectorAll('.em-faq-q').forEach(function(btn){
    btn.addEventListener('click',function(){
      var expanded=this.getAttribute('aria-expanded')==='true';
      var id=this.getAttribute('aria-controls');
      var ans=document.getElementById(id);
      document.querySelectorAll('.em-faq-q').forEach(function(b){
        b.setAttribute('aria-expanded','false');
        var a=document.getElementById(b.getAttribute('aria-controls'));
        if(a) a.style.maxHeight='0';
      });
      if(!expanded){this.setAttribute('aria-expanded','true');ans.style.maxHeight=ans.scrollHeight+'px';}
    });
  });
})();
</script>

<?php get_footer(); ?>
