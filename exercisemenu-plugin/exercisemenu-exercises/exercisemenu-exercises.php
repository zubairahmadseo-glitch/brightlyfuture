<?php
/**
 * Plugin Name: ExerciseMenu Exercises
 * Plugin URI:  https://exercisemenu.com
 * Description: Custom Post Type and meta boxes for Exercise pages on ExerciseMenu.com
 * Version:     1.1.0
 * Author:      ExerciseMenu
 * Text Domain: exercisemenu
 *
 * CHANGELOG v1.1.0
 * - SEO fields now defer to Rank Math (plugin no longer outputs <title>/<meta description>)
 * - GIF field upgraded to Media Library picker (old URL preserved as fallback)
 * - GIF frontend output now has width/height/loading="lazy"
 * - How-To Steps: Title limited to 60 chars with counter; Description required
 * - FAQ answers trimmed of leading/trailing spaces and stray colons on save
 * - "Approx. Calories per set" renamed to "Estimated Calories per set" + frontend note
 * - Removed "ACSM guidelines" hint from Sets & Reps table
 * - Modifications: added optional "Link to exercise page" post picker
 * - Related Articles: upgraded to post picker (legacy text URL still rendered)
 * - NEW: Alternative Exercises meta box (2–4 exercise pickers with GIF thumbnails)
 * - NEW: Sources meta box (citation + URL repeater, rendered before FAQs)
 * - NEW: Muscle Map Image meta box (optional image shown next to Muscles Worked)
 * - NEW: Workout Plans Using This Exercise meta box (manual repeater)
 * - NEW: "Last updated" date shown near top of page
 * - Schema: removed HowTo (deprecated by Google 2023); added Article + ImageObject
 * - REST API: post type + all plugin fields registered with show_in_rest + auth
 */

if ( ! defined( 'ABSPATH' ) ) exit;

// ─────────────────────────────────────────────
// 1. REGISTER CUSTOM POST TYPE
// ─────────────────────────────────────────────
function em_register_exercise_cpt() {
    $labels = [
        'name'               => 'Exercises',
        'singular_name'      => 'Exercise',
        'add_new'            => 'Add New Exercise',
        'add_new_item'       => 'Add New Exercise',
        'edit_item'          => 'Edit Exercise',
        'new_item'           => 'New Exercise',
        'view_item'          => 'View Exercise',
        'search_items'       => 'Search Exercises',
        'not_found'          => 'No exercises found',
        'not_found_in_trash' => 'No exercises found in trash',
        'menu_name'          => 'Exercises',
    ];

    register_post_type( 'exercise', [
        'labels'             => $labels,
        'public'             => true,
        'has_archive'        => true,
        'rewrite'            => [ 'slug' => 'exercises' ],
        'supports'           => [ 'title', 'thumbnail' ],
        'menu_icon'          => 'dashicons-heart',
        'show_in_rest'       => false,
        'menu_position'      => 5,
    ]);
}
add_action( 'init', 'em_register_exercise_cpt' );

// Flush rewrite rules on activation
register_activation_hook( __FILE__, function() {
    em_register_exercise_cpt();
    flush_rewrite_rules();
});
register_deactivation_hook( __FILE__, 'flush_rewrite_rules' );


// ─────────────────────────────────────────────
// 2. REGISTER ALL META BOXES
// ─────────────────────────────────────────────
function em_register_meta_boxes() {
    add_meta_box( 'em_seo',           'SEO & Meta (Legacy — see Rank Math)', 'em_render_seo_box',   'exercise', 'normal', 'high' );
    add_meta_box( 'em_basics',        'Exercise Basics',             'em_render_basics_box',        'exercise', 'normal', 'high' );
    add_meta_box( 'em_gif',           'GIF / Media',                 'em_render_gif_box',           'exercise', 'normal', 'high' );
    add_meta_box( 'em_quick_answer',  'Quick Answer (AEO)',          'em_render_qa_box',            'exercise', 'normal', 'high' );
    add_meta_box( 'em_muscles',       'Muscles Worked',              'em_render_muscles_box',       'exercise', 'normal', 'default' );
    add_meta_box( 'em_muscle_map',    'Muscle Map Image (optional)', 'em_render_muscle_map_box',    'exercise', 'normal', 'default' );
    add_meta_box( 'em_steps',         'How-To Steps',                'em_render_steps_box',         'exercise', 'normal', 'default' );
    add_meta_box( 'em_sets_reps',     'Sets & Reps Table',           'em_render_sets_box',          'exercise', 'normal', 'default' );
    add_meta_box( 'em_mistakes',      'Common Mistakes',             'em_render_mistakes_box',      'exercise', 'normal', 'default' );
    add_meta_box( 'em_tips',          'Tips',                        'em_render_tips_box',          'exercise', 'normal', 'default' );
    add_meta_box( 'em_mods',          'Modifications (Easier/Harder)', 'em_render_mods_box',        'exercise', 'normal', 'default' );
    add_meta_box( 'em_alt_exercises', 'Alternative Exercises',       'em_render_alt_exercises_box', 'exercise', 'normal', 'default' );
    add_meta_box( 'em_sources',       'Sources (Citations)',         'em_render_sources_box',       'exercise', 'normal', 'default' );
    add_meta_box( 'em_faqs',          'FAQs',                        'em_render_faqs_box',          'exercise', 'normal', 'default' );
    add_meta_box( 'em_workout_plans', 'Workout Plans Using This Exercise', 'em_render_workout_plans_box', 'exercise', 'normal', 'default' );
    add_meta_box( 'em_related',       'Related Articles',            'em_render_related_box',       'exercise', 'side',   'default' );
    add_meta_box( 'em_sidebar_plans', 'Sidebar Workout Plans',       'em_render_plans_box',         'exercise', 'side',   'default' );
}
add_action( 'add_meta_boxes', 'em_register_meta_boxes' );


// ─────────────────────────────────────────────
// 3. HELPER: nonce field
// ─────────────────────────────────────────────
function em_nonce_field( $action ) {
    wp_nonce_field( $action, $action . '_nonce' );
}
function em_verify_nonce( $action ) {
    return isset( $_POST[ $action . '_nonce' ] ) &&
           wp_verify_nonce( $_POST[ $action . '_nonce' ], $action );
}


// ─────────────────────────────────────────────
// 4. ADMIN STYLES
// ─────────────────────────────────────────────
function em_admin_styles( $hook ) {
    if ( ! in_array( $hook, [ 'post.php', 'post-new.php' ] ) ) return;
    global $post;
    if ( ! $post || $post->post_type !== 'exercise' ) return;
    echo '<style>
    .em-meta-box { padding: 4px 0; }
    .em-field-group { margin-bottom: 14px; }
    .em-field-group label { display: block; font-weight: 600; margin-bottom: 4px; font-size: 13px; }
    .em-field-group input[type=text], .em-field-group textarea, .em-field-group select {
        width: 100%; padding: 7px 10px; border: 1px solid #ccd0d4; border-radius: 4px;
        font-size: 13px; background: #fff; box-sizing: border-box;
    }
    .em-field-group textarea { min-height: 70px; resize: vertical; }
    .em-repeater-row { background: #f9f9f9; border: 1px solid #e0e0e0; border-radius: 6px; padding: 12px; margin-bottom: 10px; position: relative; }
    .em-repeater-row .em-remove-row { position: absolute; top: 8px; right: 10px; background: #c0392b; color: #fff; border: none; border-radius: 3px; cursor: pointer; padding: 2px 8px; font-size: 12px; }
    .em-add-row { background: #1d2327; color: #fff; border: none; border-radius: 4px; padding: 7px 14px; cursor: pointer; font-size: 13px; margin-top: 6px; }
    .em-add-row:hover { background: #c0392b; }
    .em-hint { font-size: 11px; color: #888; margin-top: 3px; }
    .em-char-count { font-size: 11px; color: #888; float: right; }
    .em-char-over { color: #c0392b; font-weight: 700; }
    table.em-sets-table { width: 100%; border-collapse: collapse; font-size: 13px; }
    table.em-sets-table th, table.em-sets-table td { padding: 7px 10px; border: 1px solid #ddd; text-align: left; }
    table.em-sets-table th { background: #f1f1f1; font-weight: 600; }
    table.em-sets-table input { width: 100%; border: none; background: transparent; padding: 2px 0; font-size: 13px; }
    </style>';
}
add_action( 'admin_head', 'em_admin_styles' );


// ─────────────────────────────────────────────
// 5. RENDER META BOXES
// ─────────────────────────────────────────────

// SEO (legacy — Rank Math now controls <title> and meta description output)
function em_render_seo_box( $post ) {
    em_nonce_field( 'em_seo' );
    $meta_title = get_post_meta( $post->ID, '_em_meta_title', true );
    $meta_desc  = get_post_meta( $post->ID, '_em_meta_desc', true );
    $rm_title   = get_post_meta( $post->ID, 'rank_math_title',       true );
    $rm_desc    = get_post_meta( $post->ID, 'rank_math_description', true );
    $has_rm     = defined('RANK_MATH_VERSION') || function_exists('rank_math');

    echo '<div class="em-meta-box">
    <div style="background:#fff3cd;border-left:4px solid #ffc107;padding:10px 14px;margin-bottom:14px;border-radius:4px;font-size:12px;line-height:1.5;">
        <strong>Note:</strong> SEO is now handled by Rank Math. Edit Meta Title and Meta Description in the <strong>Rank Math SEO</strong> box below. These legacy fields are shown for reference only and no longer output to the page.
        ' . ( $has_rm ? '' : '<br><strong style="color:#c0392b">⚠ Rank Math is not active.</strong> Enable it or the page will have no SEO meta tags.' ) . '
    </div>
    <div class="em-field-group">
        <label>Legacy Meta Title <span class="em-char-count" id="mt-count">' . strlen($meta_title) . '/60</span></label>
        <input type="text" name="em_meta_title" id="em_meta_title" value="' . esc_attr($meta_title) . '" maxlength="70" oninput="document.getElementById(\'mt-count\').textContent=this.value.length+\'/60\';document.getElementById(\'mt-count\').className=this.value.length>60?\'em-char-count em-char-over\':\'em-char-count\'">
        <p class="em-hint">Current Rank Math title: <code>' . ( $rm_title ? esc_html($rm_title) : '<em>(empty)</em>' ) . '</code></p>
    </div>
    <div class="em-field-group">
        <label>Legacy Meta Description <span class="em-char-count" id="md-count">' . strlen($meta_desc) . '/155</span></label>
        <textarea name="em_meta_desc" id="em_meta_desc" maxlength="180" oninput="document.getElementById(\'md-count\').textContent=this.value.length+\'/155\';document.getElementById(\'md-count\').className=this.value.length>155?\'em-char-count em-char-over\':\'em-char-count\'">' . esc_textarea($meta_desc) . '</textarea>
        <p class="em-hint">Current Rank Math description: <code>' . ( $rm_desc ? esc_html($rm_desc) : '<em>(empty)</em>' ) . '</code></p>
    </div>
    <div class="em-field-group">
        <label><input type="checkbox" name="em_copy_to_rankmath" value="1"> Copy these legacy values to Rank Math on save (overwrites current Rank Math values)</label>
    </div>
    </div>';
}

// Basics
function em_render_basics_box( $post ) {
    em_nonce_field( 'em_basics' );
    $fields = [
        '_em_subtitle'        => [ 'Subtitle (one line description)', 'text' ],
        '_em_tags'            => [ 'Tags (comma-separated: Beginner, Isolation, Dumbbells…)', 'text' ],
        '_em_target_muscle'   => [ 'Target Muscle (sidebar display)', 'text' ],
        '_em_body_part'       => [ 'Body Part', 'text' ],
        '_em_equipment'       => [ 'Equipment', 'text' ],
        '_em_category'        => [ 'Category (Isolation / Compound)', 'text' ],
        '_em_skill_level'     => [ 'Skill Level', 'select', [ 'Beginner', 'Intermediate', 'Advanced' ] ],
        '_em_movement'        => [ 'Movement Pattern (e.g. Elbow Flexion)', 'text' ],
        '_em_also_known_as'   => [ 'Also Known As', 'text' ],
        '_em_calories'        => [ 'Estimated Calories per set (e.g. 3–5 kcal)', 'text' ],
    ];
    echo '<div class="em-meta-box">';
    foreach ( $fields as $key => $field ) {
        $val = get_post_meta( $post->ID, $key, true );
        echo '<div class="em-field-group"><label>' . esc_html($field[0]) . '</label>';
        if ( $field[1] === 'select' ) {
            echo '<select name="' . esc_attr( ltrim($key, '_') ) . '">';
            foreach ( $field[2] as $opt ) {
                echo '<option value="' . esc_attr($opt) . '"' . selected($val, $opt, false) . '>' . esc_html($opt) . '</option>';
            }
            echo '</select>';
        } else {
            echo '<input type="text" name="' . esc_attr( ltrim($key, '_') ) . '" value="' . esc_attr($val) . '">';
        }
        echo '</div>';
    }
    echo '</div>';
}

// GIF — v1.1 adds Media Library picker; legacy URL preserved as fallback
function em_render_gif_box( $post ) {
    em_nonce_field( 'em_gif' );
    $gif_url     = get_post_meta( $post->ID, '_em_gif_url', true );
    $gif_alt     = get_post_meta( $post->ID, '_em_gif_alt', true );
    $gif_media_id = (int) get_post_meta( $post->ID, '_em_gif_media_id', true );
    $preview_src = '';
    $preview_w   = '';
    $preview_h   = '';
    if ( $gif_media_id ) {
        $preview_src = wp_get_attachment_url( $gif_media_id );
        $meta = wp_get_attachment_metadata( $gif_media_id );
        if ( ! empty($meta['width']) )  $preview_w = $meta['width'];
        if ( ! empty($meta['height']) ) $preview_h = $meta['height'];
    } elseif ( $gif_url ) {
        $preview_src = $gif_url;
    }
    echo '<div class="em-meta-box">
    <div class="em-field-group">
        <label>GIF (upload from Media Library)</label>
        <input type="hidden" name="em_gif_media_id" id="em_gif_media_id" value="' . esc_attr($gif_media_id) . '">
        <div id="em-gif-preview" style="margin-bottom:8px;' . ( $preview_src ? '' : 'display:none;' ) . '">
            <img src="' . esc_url($preview_src) . '" style="max-width:260px;max-height:160px;border:1px solid #ddd;border-radius:4px;background:#f8f9fa;" alt="">
            <p style="font-size:11px;color:#888;margin:4px 0 0;">Dimensions: ' . ( $preview_w && $preview_h ? esc_html("{$preview_w} × {$preview_h}px") : '<em>unknown</em>' ) . '</p>
        </div>
        <button type="button" class="button" id="em-gif-upload-btn">Choose / Upload GIF</button>
        <button type="button" class="button" id="em-gif-clear-btn" style="' . ( $gif_media_id ? '' : 'display:none;' ) . '">Clear</button>
    </div>
    <div class="em-field-group">
        <label>Legacy GIF URL (fallback if no Media Library file is selected)</label>
        <input type="text" name="em_gif_url" value="' . esc_attr($gif_url) . '" placeholder="https://cdn.exercisemenu.com/gifs/dumbbell-biceps-curl.gif">
    </div>
    <div class="em-field-group">
        <label>GIF Alt Text</label>
        <input type="text" name="em_gif_alt" value="' . esc_attr($gif_alt) . '" placeholder="Dumbbell Biceps Curl exercise animation — proper form demonstration">
    </div>
    </div>
    <script>
    jQuery(function($){
        var frame;
        $("#em-gif-upload-btn").on("click", function(e){
            e.preventDefault();
            if (frame) { frame.open(); return; }
            frame = wp.media({ title: "Select or Upload GIF", button: { text: "Use this file" }, library: { type: "image" }, multiple: false });
            frame.on("select", function(){
                var att = frame.state().get("selection").first().toJSON();
                $("#em_gif_media_id").val(att.id);
                var img = "<img src=\"" + att.url + "\" style=\"max-width:260px;max-height:160px;border:1px solid #ddd;border-radius:4px;background:#f8f9fa;\" alt=\"\">";
                var dim = (att.width && att.height) ? att.width + " × " + att.height + "px" : "unknown";
                $("#em-gif-preview").html(img + "<p style=\"font-size:11px;color:#888;margin:4px 0 0;\">Dimensions: " + dim + "</p>").show();
                $("#em-gif-clear-btn").show();
            });
            frame.open();
        });
        $("#em-gif-clear-btn").on("click", function(e){
            e.preventDefault();
            $("#em_gif_media_id").val("");
            $("#em-gif-preview").hide();
            $(this).hide();
        });
    });
    </script>';
}
// Enqueue WP media uploader
add_action( 'admin_enqueue_scripts', function( $hook ) {
    if ( ! in_array( $hook, [ 'post.php', 'post-new.php' ] ) ) return;
    global $post;
    if ( ! $post || $post->post_type !== 'exercise' ) return;
    wp_enqueue_media();
});

// Quick Answer
function em_render_qa_box( $post ) {
    em_nonce_field( 'em_quick_answer' );
    $qa = get_post_meta( $post->ID, '_em_quick_answer', true );
    echo '<div class="em-meta-box">
    <div class="em-field-group">
        <label>Quick Answer Text <span class="em-char-count" id="qa-count">' . strlen($qa) . '/320</span></label>
        <textarea name="em_quick_answer" maxlength="400" oninput="document.getElementById(\'qa-count\').textContent=this.value.length+\'/320\';document.getElementById(\'qa-count\').className=this.value.length>320?\'em-char-count em-char-over\':\'em-char-count\'">' . esc_textarea($qa) . '</textarea>
        <p class="em-hint">Must be under 60 words AND under 320 characters simultaneously (AEO requirement).</p>
    </div>
    </div>';
}

// Muscles
function em_render_muscles_box( $post ) {
    em_nonce_field( 'em_muscles' );
    $primary   = get_post_meta( $post->ID, '_em_primary_muscles', true ) ?: [];
    $secondary = get_post_meta( $post->ID, '_em_secondary_muscles', true ) ?: [];
    if ( ! is_array($primary) )   $primary   = array_filter( explode(',', $primary) );
    if ( ! is_array($secondary) ) $secondary = array_filter( explode(',', $secondary) );
    echo '<div class="em-meta-box">
    <div class="em-field-group">
        <label>Primary Muscles (one per line)</label>
        <textarea name="em_primary_muscles" placeholder="Biceps Brachii Long Head&#10;Biceps Brachii Short Head">' . esc_textarea( implode("\n", $primary) ) . '</textarea>
    </div>
    <div class="em-field-group">
        <label>Secondary Muscles (one per line)</label>
        <textarea name="em_secondary_muscles" placeholder="Brachialis&#10;Brachioradialis">' . esc_textarea( implode("\n", $secondary) ) . '</textarea>
    </div>
    </div>';
}

// How-To Steps (repeater)
function em_render_steps_box( $post ) {
    em_nonce_field( 'em_steps' );
    $steps = get_post_meta( $post->ID, '_em_steps', true ) ?: [];
    if ( empty($steps) ) $steps = [ [ 'title' => '', 'desc' => '' ] ];
    echo '<div class="em-meta-box">
    <div id="em-steps-wrap">';
    foreach ( $steps as $i => $step ) {
        $t_len = strlen($step['title']);
        echo '<div class="em-repeater-row">
            <button type="button" class="em-remove-row" onclick="emRemoveRow(this)">✕ Remove</button>
            <div class="em-field-group">
                <label>Step ' . ($i+1) . ' Title <span class="em-char-count em-step-count" data-max="60">' . $t_len . '/60</span></label>
                <input type="text" class="em-step-title" name="em_steps[' . $i . '][title]" value="' . esc_attr($step['title']) . '" maxlength="60" placeholder="e.g. Brace your core and stand tall">
            </div>
            <div class="em-field-group">
                <label>Step ' . ($i+1) . ' Description <span style="color:#c0392b">*</span></label>
                <textarea class="em-step-desc" name="em_steps[' . $i . '][desc]" required placeholder="Detail what to do in this step... (required)">' . esc_textarea($step['desc']) . '</textarea>
            </div>
        </div>';
    }
    echo '</div>
    <button type="button" class="em-add-row" onclick="emAddStep()">+ Add Step</button>
    <p class="em-hint">Step title is limited to 60 characters. Description is required for each step.</p>
    </div>
    <script>
    var emStepCount = ' . count($steps) . ';
    function emAddStep() {
        var i = emStepCount++;
        var wrap = document.getElementById("em-steps-wrap");
        var row = document.createElement("div");
        row.className = "em-repeater-row";
        row.innerHTML = \'<button type="button" class="em-remove-row" onclick="emRemoveRow(this)">✕ Remove</button><div class="em-field-group"><label>Step Title <span class="em-char-count em-step-count" data-max="60">0/60</span></label><input type="text" class="em-step-title" name="em_steps[\'+i+\'][title]" maxlength="60" placeholder="Step title"></div><div class="em-field-group"><label>Step Description <span style="color:#c0392b">*</span></label><textarea class="em-step-desc" name="em_steps[\'+i+\'][desc]" required placeholder="Step detail... (required)"></textarea></div>\';
        wrap.appendChild(row);
        bindStepCounters();
    }
    function emRemoveRow(btn) { btn.closest(".em-repeater-row").remove(); }
    function bindStepCounters() {
        document.querySelectorAll(".em-step-title").forEach(function(input){
            if (input.dataset.bound) return;
            input.dataset.bound = "1";
            input.addEventListener("input", function(){
                var counter = this.parentNode.querySelector(".em-step-count");
                if (!counter) return;
                counter.textContent = this.value.length + "/60";
                counter.className = this.value.length > 60 ? "em-char-count em-step-count em-char-over" : "em-char-count em-step-count";
            });
        });
    }
    bindStepCounters();
    </script>';
}

// Sets & Reps
function em_render_sets_box( $post ) {
    em_nonce_field( 'em_sets_reps' );
    $defaults = [
        [ 'goal' => 'Muscle Growth', 'sets' => '3–4', 'reps' => '8–12',  'rest' => '60–90 sec' ],
        [ 'goal' => 'Strength',      'sets' => '3–5', 'reps' => '4–6',   'rest' => '3–5 min'   ],
        [ 'goal' => 'Endurance',     'sets' => '2–3', 'reps' => '15–20', 'rest' => '30–60 sec' ],
        [ 'goal' => 'Beginner',      'sets' => '2–3', 'reps' => '10–12', 'rest' => '60–90 sec' ],
    ];
    $rows = get_post_meta( $post->ID, '_em_sets_reps', true ) ?: $defaults;
    echo '<div class="em-meta-box">
    <table class="em-sets-table">
        <thead><tr><th>Goal</th><th>Sets</th><th>Reps</th><th>Rest</th></tr></thead>
        <tbody>';
    foreach ( $rows as $i => $row ) {
        echo '<tr>
            <td><input type="text" name="em_sets_reps[' . $i . '][goal]" value="' . esc_attr($row['goal']) . '"></td>
            <td><input type="text" name="em_sets_reps[' . $i . '][sets]" value="' . esc_attr($row['sets']) . '"></td>
            <td><input type="text" name="em_sets_reps[' . $i . '][reps]" value="' . esc_attr($row['reps']) . '"></td>
            <td><input type="text" name="em_sets_reps[' . $i . '][rest]" value="' . esc_attr($row['rest']) . '"></td>
        </tr>';
    }
    echo '</tbody></table>
    <p class="em-hint">Edit values directly in the table.</p>
    </div>';
}

// Mistakes (repeater)
function em_render_mistakes_box( $post ) {
    em_nonce_field( 'em_mistakes' );
    $items = get_post_meta( $post->ID, '_em_mistakes', true ) ?: [ '' ];
    echo '<div class="em-meta-box"><div id="em-mistakes-wrap">';
    foreach ( $items as $i => $item ) {
        echo '<div class="em-repeater-row">
            <button type="button" class="em-remove-row" onclick="emRemoveRow(this)">✕ Remove</button>
            <div class="em-field-group">
                <label>Mistake ' . ($i+1) . '</label>
                <textarea name="em_mistakes[' . $i . ']" placeholder="Describe the mistake and why it reduces results...">' . esc_textarea($item) . '</textarea>
            </div>
        </div>';
    }
    echo '</div>
    <button type="button" class="em-add-row" onclick="emAddItem(\'em-mistakes-wrap\',\'em_mistakes\',\'Mistake\')">+ Add Mistake</button>
    </div>
    <script>
    function emAddItem(wrapId, fieldName, label) {
        var wrap = document.getElementById(wrapId);
        var i = wrap.querySelectorAll(".em-repeater-row").length;
        var row = document.createElement("div");
        row.className = "em-repeater-row";
        row.innerHTML = \'<button type="button" class="em-remove-row" onclick="emRemoveRow(this)">✕ Remove</button><div class="em-field-group"><label>\'+label+\'</label><textarea name="\'+fieldName+\'[\'+i+\']" placeholder="Detail..."></textarea></div>\';
        wrap.appendChild(row);
    }
    </script>';
}

// Tips (repeater)
function em_render_tips_box( $post ) {
    em_nonce_field( 'em_tips' );
    $items = get_post_meta( $post->ID, '_em_tips', true ) ?: [ '' ];
    echo '<div class="em-meta-box"><div id="em-tips-wrap">';
    foreach ( $items as $i => $item ) {
        echo '<div class="em-repeater-row">
            <button type="button" class="em-remove-row" onclick="emRemoveRow(this)">✕ Remove</button>
            <div class="em-field-group">
                <label>Tip ' . ($i+1) . '</label>
                <textarea name="em_tips[' . $i . ']" placeholder="Tip content — include citation links as plain HTML anchor tags if needed...">' . esc_textarea($item) . '</textarea>
            </div>
        </div>';
    }
    echo '</div>
    <button type="button" class="em-add-row" onclick="emAddItem(\'em-tips-wrap\',\'em_tips\',\'Tip\')">+ Add Tip</button>
    </div>';
}

// Modifications
function em_render_mods_box( $post ) {
    em_nonce_field( 'em_mods' );
    $defaults = [
        [ 'type' => 'easier', 'title' => '', 'desc' => '', 'link_id' => 0 ],
        [ 'type' => 'easier', 'title' => '', 'desc' => '', 'link_id' => 0 ],
        [ 'type' => 'harder', 'title' => '', 'desc' => '', 'link_id' => 0 ],
        [ 'type' => 'harder', 'title' => '', 'desc' => '', 'link_id' => 0 ],
    ];
    $mods = get_post_meta( $post->ID, '_em_mods', true ) ?: $defaults;
    $all_exercises = em_get_all_exercises_dropdown( $post->ID );
    echo '<div class="em-meta-box"><div id="em-mods-wrap">';
    foreach ( $mods as $i => $mod ) {
        $link_id = (int)( $mod['link_id'] ?? 0 );
        echo '<div class="em-repeater-row">
            <button type="button" class="em-remove-row" onclick="emRemoveRow(this)">✕ Remove</button>
            <div class="em-field-group">
                <label>Type</label>
                <select name="em_mods[' . $i . '][type]">
                    <option value="easier"' . selected($mod['type'],'easier',false) . '>🔽 Easier</option>
                    <option value="harder"' . selected($mod['type'],'harder',false) . '>🔼 Harder</option>
                </select>
            </div>
            <div class="em-field-group">
                <label>Title (e.g. Cable Bicep Curl)</label>
                <input type="text" name="em_mods[' . $i . '][title]" value="' . esc_attr($mod['title']) . '">
            </div>
            <div class="em-field-group">
                <label>Description</label>
                <textarea name="em_mods[' . $i . '][desc]">' . esc_textarea($mod['desc']) . '</textarea>
            </div>
            <div class="em-field-group">
                <label>Link to exercise page (optional)</label>
                <select name="em_mods[' . $i . '][link_id]">
                    <option value="0">— None —</option>
                    ' . em_options_html( $all_exercises, $link_id ) . '
                </select>
                <p class="em-hint">If selected, the modification title will link to this exercise page.</p>
            </div>
        </div>';
    }
    echo '</div>
    <button type="button" class="em-add-row" onclick="emAddMod()">+ Add Modification</button>
    </div>
    <script>
    var emExerciseOptions = ' . wp_json_encode( $all_exercises ) . ';
    function emAddMod() {
        var wrap = document.getElementById("em-mods-wrap");
        var i = wrap.querySelectorAll(".em-repeater-row").length;
        var row = document.createElement("div");
        row.className = "em-repeater-row";
        var opts = \'<option value="0">— None —</option>\';
        emExerciseOptions.forEach(function(o){ opts += \'<option value="\'+o.id+\'">\'+o.title+\'</option>\'; });
        row.innerHTML = \'<button type="button" class="em-remove-row" onclick="emRemoveRow(this)">✕ Remove</button><div class="em-field-group"><label>Type</label><select name="em_mods[\'+i+\'][type]"><option value="easier">🔽 Easier</option><option value="harder">🔼 Harder</option></select></div><div class="em-field-group"><label>Title</label><input type="text" name="em_mods[\'+i+\'][title]"></div><div class="em-field-group"><label>Description</label><textarea name="em_mods[\'+i+\'][desc]"></textarea></div><div class="em-field-group"><label>Link to exercise page (optional)</label><select name="em_mods[\'+i+\'][link_id]">\'+opts+\'</select></div>\';
        wrap.appendChild(row);
    }
    </script>';
}

// Helper: get all exercise posts for dropdowns (excluding current post)
function em_get_all_exercises_dropdown( $exclude_id = 0 ) {
    $q = new WP_Query([
        'post_type'      => 'exercise',
        'posts_per_page' => -1,
        'post_status'    => [ 'publish', 'draft' ],
        'orderby'        => 'title',
        'order'          => 'ASC',
        'post__not_in'   => $exclude_id ? [ $exclude_id ] : [],
        'no_found_rows'  => true,
    ]);
    $out = [];
    foreach ( $q->posts as $p ) {
        $out[] = [ 'id' => $p->ID, 'title' => $p->post_title ];
    }
    return $out;
}

// Helper: build <option> list from a dropdown array
function em_options_html( $items, $selected_id ) {
    $html = '';
    foreach ( $items as $item ) {
        $html .= '<option value="' . esc_attr($item['id']) . '"' . selected( $selected_id, $item['id'], false ) . '>' . esc_html($item['title']) . '</option>';
    }
    return $html;
}

// FAQs (repeater)
function em_render_faqs_box( $post ) {
    em_nonce_field( 'em_faqs' );
    $faqs = get_post_meta( $post->ID, '_em_faqs', true ) ?: [ [ 'q' => '', 'a' => '' ] ];
    echo '<div class="em-meta-box"><div id="em-faqs-wrap">';
    foreach ( $faqs as $i => $faq ) {
        echo '<div class="em-repeater-row">
            <button type="button" class="em-remove-row" onclick="emRemoveRow(this)">✕ Remove</button>
            <div class="em-field-group">
                <label>Question ' . ($i+1) . '</label>
                <input type="text" name="em_faqs[' . $i . '][q]" value="' . esc_attr($faq['q']) . '" placeholder="e.g. How many sets should I do?">
            </div>
            <div class="em-field-group">
                <label>Answer ' . ($i+1) . '</label>
                <textarea name="em_faqs[' . $i . '][a]" placeholder="Answer — must contain unique info not covered in article body...">' . esc_textarea($faq['a']) . '</textarea>
            </div>
        </div>';
    }
    echo '</div>
    <button type="button" class="em-add-row" onclick="emAddFAQ()">+ Add FAQ</button>
    </div>
    <script>
    function emAddFAQ() {
        var wrap = document.getElementById("em-faqs-wrap");
        var i = wrap.querySelectorAll(".em-repeater-row").length;
        var row = document.createElement("div");
        row.className = "em-repeater-row";
        row.innerHTML = \'<button type="button" class="em-remove-row" onclick="emRemoveRow(this)">✕ Remove</button><div class="em-field-group"><label>Question</label><input type="text" name="em_faqs[\'+i+\'][q]" placeholder="FAQ question..."></div><div class="em-field-group"><label>Answer</label><textarea name="em_faqs[\'+i+\'][a]" placeholder="Answer..."></textarea></div>\';
        wrap.appendChild(row);
    }
    </script>';
}

// Related Articles — v1.1 upgraded to post picker; legacy text URLs still saved and rendered
function em_render_related_box( $post ) {
    em_nonce_field( 'em_related' );
    $related = get_post_meta( $post->ID, '_em_related', true ) ?: array_fill(0, 3, ['title'=>'','url'=>'','post_id'=>0]);
    echo '<div class="em-meta-box">';
    for ( $i = 0; $i < 3; $i++ ) {
        $item = $related[$i] ?? ['title'=>'','url'=>'','post_id'=>0];
        $post_id = (int)( $item['post_id'] ?? 0 );
        $linked_title = $post_id ? get_the_title($post_id) : '';
        echo '<div class="em-field-group" style="padding-bottom:10px;border-bottom:1px solid #eee;margin-bottom:12px;">
            <label><strong>Article ' . ($i+1) . '</strong></label>
            <label style="margin-top:6px;font-weight:400;">Pick from existing posts/pages:</label>
            <input type="text" class="em-related-search" data-idx="' . $i . '" placeholder="Type to search posts and pages..." value="' . esc_attr($linked_title) . '" autocomplete="off">
            <input type="hidden" name="em_related[' . $i . '][post_id]" id="em_related_pid_' . $i . '" value="' . esc_attr($post_id) . '">
            <div class="em-related-results" id="em_related_results_' . $i . '" style="display:none;background:#fff;border:1px solid #ccc;max-height:180px;overflow-y:auto;position:relative;z-index:1;"></div>
            <label style="margin-top:10px;font-weight:400;">OR legacy manual entry (overrides picker if filled):</label>
            <input type="text" name="em_related[' . $i . '][title]" value="' . esc_attr($item['title'] ?? '') . '" placeholder="e.g. What Are Reps and Sets?">
            <input type="text" name="em_related[' . $i . '][url]"   value="' . esc_attr($item['url'] ?? '') . '" placeholder="/what-are-reps-and-sets/" style="margin-top:4px;">
        </div>';
    }
    echo '</div>
    <script>
    jQuery(function($){
        $(".em-related-search").on("input", function(){
            var $input = $(this), q = $input.val(), idx = $input.data("idx");
            if (q.length < 2) { $("#em_related_results_"+idx).hide().empty(); return; }
            $.get(ajaxurl, { action: "em_search_posts", q: q, _wpnonce: "' . wp_create_nonce('em_search_posts') . '" }, function(items){
                var $box = $("#em_related_results_"+idx).empty().show();
                if (!items.length) { $box.append("<div style=\"padding:6px 10px;color:#999\">No matches</div>"); return; }
                items.forEach(function(it){
                    $("<div/>", { css: { padding:"6px 10px", cursor:"pointer", borderBottom:"1px solid #f0f0f0" } })
                        .text(it.title + " [" + it.type + "]")
                        .on("click", function(){
                            $input.val(it.title);
                            $("#em_related_pid_"+idx).val(it.id);
                            $box.hide();
                        }).appendTo($box);
                });
            });
        });
    });
    </script>';
}
// AJAX: search posts/pages
add_action( 'wp_ajax_em_search_posts', function() {
    check_ajax_referer( 'em_search_posts' );
    if ( ! current_user_can( 'edit_posts' ) ) wp_die( '', '', 403 );
    $q = sanitize_text_field( $_GET['q'] ?? '' );
    if ( strlen($q) < 2 ) wp_send_json( [] );
    $query = new WP_Query([
        'post_type'      => [ 'post', 'page' ],
        'posts_per_page' => 10,
        's'              => $q,
        'post_status'    => 'publish',
    ]);
    $out = [];
    foreach ( $query->posts as $p ) {
        $out[] = [ 'id' => $p->ID, 'title' => $p->post_title, 'type' => $p->post_type ];
    }
    wp_send_json( $out );
});

// ─── NEW v1.1 BOXES ─────────────────────────

// Alternative Exercises
function em_render_alt_exercises_box( $post ) {
    em_nonce_field( 'em_alt_exercises' );
    $alts = get_post_meta( $post->ID, '_em_alt_exercises', true ) ?: [ 0, 0, 0, 0 ];
    $all_exercises = em_get_all_exercises_dropdown( $post->ID );
    echo '<div class="em-meta-box">
        <p class="em-hint">Pick 2–4 alternative exercises. They render as cards with GIF thumbnails at the bottom of the page.</p>';
    for ( $i = 0; $i < 4; $i++ ) {
        $sel = (int)( $alts[$i] ?? 0 );
        echo '<div class="em-field-group">
            <label>Alternative ' . ($i+1) . '</label>
            <select name="em_alt_exercises[' . $i . ']">
                <option value="0">— None —</option>
                ' . em_options_html( $all_exercises, $sel ) . '
            </select>
        </div>';
    }
    echo '</div>';
}

// Sources (citations)
function em_render_sources_box( $post ) {
    em_nonce_field( 'em_sources' );
    $sources = get_post_meta( $post->ID, '_em_sources', true ) ?: [ [ 'text' => '', 'url' => '' ] ];
    echo '<div class="em-meta-box"><div id="em-sources-wrap">';
    foreach ( $sources as $i => $src ) {
        echo '<div class="em-repeater-row">
            <button type="button" class="em-remove-row" onclick="emRemoveRow(this)">✕ Remove</button>
            <div class="em-field-group">
                <label>Citation Text</label>
                <input type="text" name="em_sources[' . $i . '][text]" value="' . esc_attr($src['text'] ?? '') . '" placeholder="e.g. Solstad et al., 2020, Journal of Sports Science and Medicine">
            </div>
            <div class="em-field-group">
                <label>URL</label>
                <input type="text" name="em_sources[' . $i . '][url]" value="' . esc_attr($src['url'] ?? '') . '" placeholder="https://pubmed.ncbi.nlm.nih.gov/XXXXXXXX/">
            </div>
        </div>';
    }
    echo '</div>
    <button type="button" class="em-add-row" onclick="emAddSource()">+ Add Source</button>
    </div>
    <script>
    function emAddSource(){
        var wrap=document.getElementById("em-sources-wrap");
        var i=wrap.querySelectorAll(".em-repeater-row").length;
        var row=document.createElement("div");
        row.className="em-repeater-row";
        row.innerHTML=\'<button type="button" class="em-remove-row" onclick="emRemoveRow(this)">✕ Remove</button><div class="em-field-group"><label>Citation Text</label><input type="text" name="em_sources[\'+i+\'][text]" placeholder="Author et al., Year, Journal"></div><div class="em-field-group"><label>URL</label><input type="text" name="em_sources[\'+i+\'][url]" placeholder="https://..."></div>\';
        wrap.appendChild(row);
    }
    </script>';
}

// Muscle Map (optional image)
function em_render_muscle_map_box( $post ) {
    em_nonce_field( 'em_muscle_map' );
    $media_id = (int) get_post_meta( $post->ID, '_em_muscle_map_id', true );
    $src = $media_id ? wp_get_attachment_url( $media_id ) : '';
    echo '<div class="em-meta-box">
    <div class="em-field-group">
        <label>Muscle Map Image (optional — shown next to Muscles Worked)</label>
        <input type="hidden" name="em_muscle_map_id" id="em_muscle_map_id" value="' . esc_attr($media_id) . '">
        <div id="em-mm-preview" style="margin-bottom:8px;' . ( $src ? '' : 'display:none;' ) . '">
            <img src="' . esc_url($src) . '" style="max-width:200px;max-height:260px;border:1px solid #ddd;border-radius:4px;background:#f8f9fa;" alt="">
        </div>
        <button type="button" class="button" id="em-mm-btn">Choose / Upload Image</button>
        <button type="button" class="button" id="em-mm-clear" style="' . ( $media_id ? '' : 'display:none;' ) . '">Clear</button>
    </div>
    </div>
    <script>
    jQuery(function($){
        var frame;
        $("#em-mm-btn").on("click", function(e){
            e.preventDefault();
            if (frame) { frame.open(); return; }
            frame = wp.media({ title: "Select muscle map image", button: { text: "Use this" }, library: { type: "image" }, multiple: false });
            frame.on("select", function(){
                var att = frame.state().get("selection").first().toJSON();
                $("#em_muscle_map_id").val(att.id);
                $("#em-mm-preview").html(\'<img src="\'+att.url+\'" style="max-width:200px;max-height:260px;border:1px solid #ddd;border-radius:4px;background:#f8f9fa;" alt="">\').show();
                $("#em-mm-clear").show();
            });
            frame.open();
        });
        $("#em-mm-clear").on("click", function(e){
            e.preventDefault();
            $("#em_muscle_map_id").val("");
            $("#em-mm-preview").hide();
            $(this).hide();
        });
    });
    </script>';
}

// Workout Plans Using This Exercise (manual repeater)
function em_render_workout_plans_box( $post ) {
    em_nonce_field( 'em_workout_plans' );
    $plans = get_post_meta( $post->ID, '_em_workout_plans_list', true ) ?: [ [ 'post_id' => 0, 'day_label' => '' ] ];
    echo '<div class="em-meta-box">
        <p class="em-hint">Pick workout-plan posts/pages that include this exercise. Rendered as cards after Modifications.</p>
        <div id="em-wp-wrap">';
    foreach ( $plans as $i => $plan ) {
        $pid = (int)( $plan['post_id'] ?? 0 );
        $title = $pid ? get_the_title($pid) : '';
        echo '<div class="em-repeater-row">
            <button type="button" class="em-remove-row" onclick="emRemoveRow(this)">✕ Remove</button>
            <div class="em-field-group">
                <label>Workout Plan (search posts/pages)</label>
                <input type="text" class="em-wp-search" data-idx="' . $i . '" placeholder="Type to search..." value="' . esc_attr($title) . '" autocomplete="off">
                <input type="hidden" name="em_workout_plans_list[' . $i . '][post_id]" id="em_wp_pid_' . $i . '" value="' . esc_attr($pid) . '">
                <div class="em-wp-results" id="em_wp_results_' . $i . '" style="display:none;background:#fff;border:1px solid #ccc;max-height:180px;overflow-y:auto;"></div>
            </div>
            <div class="em-field-group">
                <label>Day Label (e.g. "Push A", "Day 2 — Chest")</label>
                <input type="text" name="em_workout_plans_list[' . $i . '][day_label]" value="' . esc_attr($plan['day_label'] ?? '') . '" placeholder="Push A">
            </div>
        </div>';
    }
    echo '</div>
    <button type="button" class="em-add-row" onclick="emAddPlan()">+ Add Workout Plan</button>
    </div>
    <script>
    var emPlanCount = ' . count($plans) . ';
    function emAddPlan(){
        var wrap=document.getElementById("em-wp-wrap");
        var i=emPlanCount++;
        var row=document.createElement("div");
        row.className="em-repeater-row";
        row.innerHTML=\'<button type="button" class="em-remove-row" onclick="emRemoveRow(this)">✕ Remove</button><div class="em-field-group"><label>Workout Plan</label><input type="text" class="em-wp-search" data-idx="\'+i+\'" placeholder="Type to search..." autocomplete="off"><input type="hidden" name="em_workout_plans_list[\'+i+\'][post_id]" id="em_wp_pid_\'+i+\'" value="0"><div class="em-wp-results" id="em_wp_results_\'+i+\'" style="display:none;background:#fff;border:1px solid #ccc;max-height:180px;overflow-y:auto;"></div></div><div class="em-field-group"><label>Day Label</label><input type="text" name="em_workout_plans_list[\'+i+\'][day_label]" placeholder="e.g. Push A"></div>\';
        wrap.appendChild(row);
        bindWpSearch();
    }
    function bindWpSearch(){
        jQuery(".em-wp-search").each(function(){
            if (this.dataset.bound) return;
            this.dataset.bound = "1";
            jQuery(this).on("input", function(){
                var $input = jQuery(this), q = $input.val(), idx = $input.data("idx");
                if (q.length < 2) { jQuery("#em_wp_results_"+idx).hide().empty(); return; }
                jQuery.get(ajaxurl, { action: "em_search_posts", q: q, _wpnonce: "' . wp_create_nonce('em_search_posts') . '" }, function(items){
                    var $box = jQuery("#em_wp_results_"+idx).empty().show();
                    if (!items.length) { $box.append("<div style=\"padding:6px 10px;color:#999\">No matches</div>"); return; }
                    items.forEach(function(it){
                        jQuery("<div/>", { css: { padding:"6px 10px", cursor:"pointer", borderBottom:"1px solid #f0f0f0" } })
                            .text(it.title + " [" + it.type + "]")
                            .on("click", function(){
                                $input.val(it.title);
                                jQuery("#em_wp_pid_"+idx).val(it.id);
                                $box.hide();
                            }).appendTo($box);
                    });
                });
            });
        });
    }
    jQuery(bindWpSearch);
    </script>';
}

// Sidebar Plans
function em_render_plans_box( $post ) {
    em_nonce_field( 'em_sidebar_plans' );
    $plans = get_post_meta( $post->ID, '_em_sidebar_plans', true ) ?: array_fill(0, 3, ['title'=>'','url'=>'','meta'=>'','coming_soon'=>'']);
    echo '<div class="em-meta-box">';
    foreach ( $plans as $i => $plan ) {
        echo '<div class="em-repeater-row">
            <div class="em-field-group">
                <label>Plan ' . ($i+1) . ' Name</label>
                <input type="text" name="em_sidebar_plans[' . $i . '][title]" value="' . esc_attr($plan['title']) . '" placeholder="e.g. Push Pull Legs Split">
            </div>
            <div class="em-field-group">
                <label>URL (leave blank if Coming Soon)</label>
                <input type="text" name="em_sidebar_plans[' . $i . '][url]" value="' . esc_attr($plan['url'] ?? '') . '" placeholder="/push-pull-legs-split/">
            </div>
            <div class="em-field-group">
                <label>Meta text (e.g. "3–6 days/week · Intermediate")</label>
                <input type="text" name="em_sidebar_plans[' . $i . '][meta]" value="' . esc_attr($plan['meta'] ?? '') . '">
            </div>
            <div class="em-field-group">
                <label><input type="checkbox" name="em_sidebar_plans[' . $i . '][coming_soon]" value="1"' . checked($plan['coming_soon'] ?? '', '1', false) . '> Mark as Coming Soon</label>
            </div>
        </div>';
    }
    echo '</div>';
}


// ─────────────────────────────────────────────
// 6. SAVE ALL META
// ─────────────────────────────────────────────
function em_save_meta( $post_id ) {
    if ( defined('DOING_AUTOSAVE') && DOING_AUTOSAVE ) return;
    if ( ! current_user_can( 'edit_post', $post_id ) ) return;

    // Rank Math SEO sync (if user ticked the Copy checkbox)
    if ( em_verify_nonce('em_seo') && ! empty($_POST['em_copy_to_rankmath']) ) {
        if ( ! empty($_POST['em_meta_title']) ) {
            update_post_meta( $post_id, 'rank_math_title', sanitize_text_field( $_POST['em_meta_title'] ) );
        }
        if ( ! empty($_POST['em_meta_desc']) ) {
            update_post_meta( $post_id, 'rank_math_description', sanitize_textarea_field( $_POST['em_meta_desc'] ) );
        }
    }

    // GIF media id (new in v1.1)
    if ( em_verify_nonce('em_gif') ) {
        if ( isset($_POST['em_gif_media_id']) ) {
            update_post_meta( $post_id, '_em_gif_media_id', (int) $_POST['em_gif_media_id'] );
        }
    }

    // Muscle map image id
    if ( em_verify_nonce('em_muscle_map') ) {
        update_post_meta( $post_id, '_em_muscle_map_id', (int)( $_POST['em_muscle_map_id'] ?? 0 ) );
    }

    $simple_fields = [
        'em_seo'           => [ '_em_meta_title', '_em_meta_desc' ],
        'em_gif'           => [ '_em_gif_url', '_em_gif_alt' ],
        'em_quick_answer'  => [ '_em_quick_answer' ],
        'em_basics'        => [ '_em_subtitle','_em_tags','_em_target_muscle','_em_body_part',
                                '_em_equipment','_em_category','_em_skill_level','_em_movement',
                                '_em_also_known_as','_em_calories' ],
    ];

    foreach ( $simple_fields as $nonce => $keys ) {
        if ( ! em_verify_nonce( $nonce ) ) continue;
        foreach ( $keys as $key ) {
            // Field name in the form is the meta key itself (e.g. _em_subtitle)
            // $_POST strips leading underscores from field names, so _em_subtitle arrives as em_subtitle
            // We check both the raw key and the underscore-stripped version to be safe
            $post_key_raw      = $key;                         // _em_subtitle
            $post_key_stripped = ltrim( $key, '_' );           // em_subtitle
            if ( isset( $_POST[ $post_key_stripped ] ) ) {
                update_post_meta( $post_id, $key, sanitize_textarea_field( $_POST[ $post_key_stripped ] ) );
            } elseif ( isset( $_POST[ $post_key_raw ] ) ) {
                update_post_meta( $post_id, $key, sanitize_textarea_field( $_POST[ $post_key_raw ] ) );
            }
        }
    }

    // Muscles
    if ( em_verify_nonce('em_muscles') ) {
        $primary   = isset($_POST['em_primary_muscles'])   ? array_filter(array_map('sanitize_text_field', explode("\n", $_POST['em_primary_muscles'])))   : [];
        $secondary = isset($_POST['em_secondary_muscles']) ? array_filter(array_map('sanitize_text_field', explode("\n", $_POST['em_secondary_muscles']))) : [];
        update_post_meta( $post_id, '_em_primary_muscles',   $primary );
        update_post_meta( $post_id, '_em_secondary_muscles', $secondary );
    }

    // Steps
    if ( em_verify_nonce('em_steps') && isset($_POST['em_steps']) ) {
        $steps = [];
        foreach ( $_POST['em_steps'] as $step ) {
            $steps[] = [
                'title' => sanitize_text_field( $step['title'] ?? '' ),
                'desc'  => sanitize_textarea_field( $step['desc'] ?? '' ),
            ];
        }
        update_post_meta( $post_id, '_em_steps', $steps );
    }

    // Sets/Reps
    if ( em_verify_nonce('em_sets_reps') && isset($_POST['em_sets_reps']) ) {
        $rows = [];
        foreach ( $_POST['em_sets_reps'] as $row ) {
            $rows[] = [
                'goal' => sanitize_text_field( $row['goal'] ?? '' ),
                'sets' => sanitize_text_field( $row['sets'] ?? '' ),
                'reps' => sanitize_text_field( $row['reps'] ?? '' ),
                'rest' => sanitize_text_field( $row['rest'] ?? '' ),
            ];
        }
        update_post_meta( $post_id, '_em_sets_reps', $rows );
    }

    // Mistakes
    if ( em_verify_nonce('em_mistakes') && isset($_POST['em_mistakes']) ) {
        $items = array_filter( array_map( 'sanitize_textarea_field', $_POST['em_mistakes'] ) );
        update_post_meta( $post_id, '_em_mistakes', array_values($items) );
    }

    // Tips
    if ( em_verify_nonce('em_tips') && isset($_POST['em_tips']) ) {
        $items = array_filter( array_map( 'wp_kses_post', $_POST['em_tips'] ) );
        update_post_meta( $post_id, '_em_tips', array_values($items) );
    }

    // Mods — v1.1 adds link_id
    if ( em_verify_nonce('em_mods') && isset($_POST['em_mods']) ) {
        $mods = [];
        foreach ( $_POST['em_mods'] as $mod ) {
            $mods[] = [
                'type'    => sanitize_text_field( $mod['type']  ?? 'easier' ),
                'title'   => sanitize_text_field( $mod['title'] ?? '' ),
                'desc'    => sanitize_textarea_field( $mod['desc'] ?? '' ),
                'link_id' => (int)( $mod['link_id'] ?? 0 ),
            ];
        }
        update_post_meta( $post_id, '_em_mods', $mods );
    }

    // FAQs — v1.1 trims leading/trailing spaces and stray colons
    if ( em_verify_nonce('em_faqs') && isset($_POST['em_faqs']) ) {
        $faqs = [];
        foreach ( $_POST['em_faqs'] as $faq ) {
            $q = sanitize_text_field( $faq['q'] ?? '' );
            $a = sanitize_textarea_field( $faq['a'] ?? '' );
            $q = trim( $q, " \t\n\r\0\x0B:" );
            $a = trim( $a, " \t\n\r\0\x0B:" );
            $faqs[] = [ 'q' => $q, 'a' => $a ];
        }
        update_post_meta( $post_id, '_em_faqs', $faqs );
    }

    // Related — v1.1 adds post_id (post picker)
    if ( em_verify_nonce('em_related') && isset($_POST['em_related']) ) {
        $related = [];
        foreach ( $_POST['em_related'] as $item ) {
            $related[] = [
                'title'   => sanitize_text_field( $item['title'] ?? '' ),
                'url'     => sanitize_text_field( $item['url']   ?? '' ),
                'post_id' => (int)( $item['post_id'] ?? 0 ),
            ];
        }
        update_post_meta( $post_id, '_em_related', $related );
    }

    // Alt Exercises
    if ( em_verify_nonce('em_alt_exercises') && isset($_POST['em_alt_exercises']) ) {
        $alts = array_values( array_filter( array_map( 'intval', (array) $_POST['em_alt_exercises'] ) ) );
        update_post_meta( $post_id, '_em_alt_exercises', $alts );
    }

    // Sources
    if ( em_verify_nonce('em_sources') && isset($_POST['em_sources']) ) {
        $sources = [];
        foreach ( $_POST['em_sources'] as $src ) {
            $text = sanitize_text_field( $src['text'] ?? '' );
            $url  = esc_url_raw( $src['url'] ?? '' );
            if ( $text || $url ) {
                $sources[] = [ 'text' => $text, 'url' => $url ];
            }
        }
        update_post_meta( $post_id, '_em_sources', $sources );
    }

    // Workout Plans Using This Exercise
    if ( em_verify_nonce('em_workout_plans') && isset($_POST['em_workout_plans_list']) ) {
        $plans_list = [];
        foreach ( $_POST['em_workout_plans_list'] as $plan ) {
            $pid = (int)( $plan['post_id'] ?? 0 );
            if ( $pid ) {
                $plans_list[] = [
                    'post_id'   => $pid,
                    'day_label' => sanitize_text_field( $plan['day_label'] ?? '' ),
                ];
            }
        }
        update_post_meta( $post_id, '_em_workout_plans_list', $plans_list );
    }

    // Sidebar Plans
    if ( em_verify_nonce('em_sidebar_plans') && isset($_POST['em_sidebar_plans']) ) {
        $plans = [];
        foreach ( $_POST['em_sidebar_plans'] as $plan ) {
            $plans[] = [
                'title'       => sanitize_text_field( $plan['title']       ?? '' ),
                'url'         => sanitize_text_field( $plan['url']         ?? '' ),
                'meta'        => sanitize_text_field( $plan['meta']        ?? '' ),
                'coming_soon' => sanitize_text_field( $plan['coming_soon'] ?? '' ),
            ];
        }
        update_post_meta( $post_id, '_em_sidebar_plans', $plans );
    }
}
add_action( 'save_post_exercise', 'em_save_meta' );


// ─────────────────────────────────────────────
// 7. HEAD OUTPUT (meta title + description)
// ─────────────────────────────────────────────
// v1.1: DISABLED — Rank Math now controls <title> and meta description.
// To re-enable (if Rank Math is removed), define EM_OUTPUT_LEGACY_META in wp-config.php.
function em_output_meta_tags() {
    if ( ! defined('EM_OUTPUT_LEGACY_META') || ! EM_OUTPUT_LEGACY_META ) return;
    if ( ! is_singular('exercise') ) return;
    $post_id = get_the_ID();
    $title   = get_post_meta( $post_id, '_em_meta_title', true );
    $desc    = get_post_meta( $post_id, '_em_meta_desc',  true );
    if ( $title ) {
        add_filter( 'pre_get_document_title', function() use ($title) { return esc_html($title); }, 99 );
    }
    if ( $desc ) {
        echo '<meta name="description" content="' . esc_attr($desc) . '">' . "\n";
    }
}
add_action( 'wp_head', 'em_output_meta_tags', 1 );

// v1.1: Suppress Rank Math's own FAQPage schema to prevent duplicates (plugin outputs FAQPage below).
add_filter( 'rank_math/snippet/rich_snippet_faqpage_entity', function( $data ) {
    if ( is_singular('exercise') ) return [];
    return $data;
});


// ─────────────────────────────────────────────
// 8. SCHEMA OUTPUT IN <head>
// ─────────────────────────────────────────────
function em_output_schema() {
    if ( ! is_singular('exercise') ) return;
    $post_id = get_the_ID();
    $post    = get_post($post_id);

    $faqs     = get_post_meta($post_id,'_em_faqs',true)       ?: [];
    $url      = get_permalink($post_id);
    $gif_media_id = (int) get_post_meta($post_id,'_em_gif_media_id',true);
    $gif_url      = $gif_media_id ? wp_get_attachment_url($gif_media_id) : get_post_meta($post_id,'_em_gif_url',true);
    $gif_alt      = get_post_meta($post_id,'_em_gif_alt',true) ?: get_the_title($post_id);

    $schema = [ '@context' => 'https://schema.org', '@graph' => [] ];

    // Article
    $article = [
        '@type'         => 'Article',
        '@id'           => $url . '#article',
        'mainEntityOfPage' => $url,
        'headline'      => get_the_title($post_id),
        'datePublished' => get_the_date('c', $post_id),
        'dateModified'  => get_the_modified_date('c', $post_id),
        'author'        => [ '@type' => 'Person', 'name' => 'Sadia Baloch' ],
        'publisher'     => [
            '@type' => 'Organization',
            'name'  => 'Exercise Menu',
            'url'   => home_url('/'),
        ],
    ];
    if ( $gif_url ) {
        $article['image'] = $gif_url;
    }
    $schema['@graph'][] = $article;

    // ImageObject (for GIF)
    if ( $gif_url ) {
        $img_obj = [
            '@type'       => 'ImageObject',
            '@id'         => $url . '#gif',
            'contentUrl'  => $gif_url,
            'name'        => get_the_title($post_id),
            'description' => $gif_alt,
        ];
        if ( $gif_media_id ) {
            $meta = wp_get_attachment_metadata($gif_media_id);
            if ( ! empty($meta['width']) )  $img_obj['width']  = (int) $meta['width'];
            if ( ! empty($meta['height']) ) $img_obj['height'] = (int) $meta['height'];
        }
        $schema['@graph'][] = $img_obj;
    }

    // FAQPage
    if ( ! empty($faqs) ) {
        $faq_entities = [];
        foreach ( $faqs as $faq ) {
            if ( empty($faq['q']) ) continue;
            $faq_entities[] = [
                '@type' => 'Question',
                'name'  => $faq['q'],
                'acceptedAnswer' => [ '@type' => 'Answer', 'text' => $faq['a'] ],
            ];
        }
        if ( ! empty($faq_entities) ) {
            $schema['@graph'][] = [ '@type' => 'FAQPage', 'mainEntity' => $faq_entities ];
        }
    }

    // BreadcrumbList
    $schema['@graph'][] = [
        '@type' => 'BreadcrumbList',
        'itemListElement' => [
            [ '@type' => 'ListItem', 'position' => 1, 'name' => 'Home',      'item' => home_url('/') ],
            [ '@type' => 'ListItem', 'position' => 2, 'name' => 'Exercises', 'item' => home_url('/exercises/') ],
            [ '@type' => 'ListItem', 'position' => 3, 'name' => get_the_title($post_id), 'item' => $url ],
        ],
    ];

    echo '<script type="application/ld+json">' . wp_json_encode($schema, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT) . '</script>' . "\n";
}
add_action( 'wp_head', 'em_output_schema' );


// ─────────────────────────────────────────────
// 9. TEMPLATE REDIRECT — use our template
// ─────────────────────────────────────────────
function em_load_exercise_template( $template ) {
    if ( is_singular('exercise') ) {
        $plugin_template = plugin_dir_path(__FILE__) . 'templates/single-exercise.php';
        if ( file_exists($plugin_template) ) {
            return $plugin_template;
        }
    }
    return $template;
}
add_filter( 'template_include', 'em_load_exercise_template' );


// ─────────────────────────────────────────────
// 10. v1.1 — REGISTER CPT WITH REST + show_in_rest ON POST TYPE
// ─────────────────────────────────────────────
// Make the exercise CPT REST-accessible, so Rank Math picks it up for sitemaps
// and so the fields can be read/written via /wp-json/wp/v2/exercises.
add_action( 'init', function() {
    global $wp_post_types;
    if ( isset( $wp_post_types['exercise'] ) ) {
        $wp_post_types['exercise']->show_in_rest          = true;
        $wp_post_types['exercise']->rest_base             = 'exercises';
        $wp_post_types['exercise']->rest_controller_class = 'WP_REST_Posts_Controller';
    }
}, 20 );


// ─────────────────────────────────────────────
// 11. v1.1 — REGISTER ALL META FIELDS FOR REST API
// ─────────────────────────────────────────────
add_action( 'init', function() {
    $auth = function() { return current_user_can('edit_posts'); };

    // Simple string fields
    $string_keys = [
        '_em_meta_title', '_em_meta_desc', '_em_subtitle', '_em_tags',
        '_em_target_muscle', '_em_body_part', '_em_equipment', '_em_category',
        '_em_skill_level', '_em_movement', '_em_also_known_as', '_em_calories',
        '_em_gif_url', '_em_gif_alt', '_em_quick_answer',
    ];
    foreach ( $string_keys as $k ) {
        register_post_meta( 'exercise', $k, [
            'type'              => 'string',
            'single'            => true,
            'show_in_rest'      => true,
            'sanitize_callback' => 'sanitize_textarea_field',
            'auth_callback'     => $auth,
        ]);
    }

    // Integer fields
    foreach ( [ '_em_gif_media_id', '_em_muscle_map_id' ] as $k ) {
        register_post_meta( 'exercise', $k, [
            'type'              => 'integer',
            'single'            => true,
            'show_in_rest'      => true,
            'sanitize_callback' => 'absint',
            'auth_callback'     => $auth,
        ]);
    }

    // Array of strings
    foreach ( [ '_em_primary_muscles', '_em_secondary_muscles', '_em_mistakes', '_em_tips' ] as $k ) {
        register_post_meta( 'exercise', $k, [
            'type'          => 'array',
            'single'        => true,
            'show_in_rest'  => [ 'schema' => [ 'items' => [ 'type' => 'string' ] ] ],
            'auth_callback' => $auth,
        ]);
    }

    // Array of integers (alt exercises)
    register_post_meta( 'exercise', '_em_alt_exercises', [
        'type'          => 'array',
        'single'        => true,
        'show_in_rest'  => [ 'schema' => [ 'items' => [ 'type' => 'integer' ] ] ],
        'auth_callback' => $auth,
    ]);

    // Complex repeaters — expose as string (JSON) for simplicity. Clients should
    // JSON-decode after read and JSON-encode before write.
    foreach ( [ '_em_steps', '_em_sets_reps', '_em_mods', '_em_faqs', '_em_related',
                '_em_sources', '_em_workout_plans_list', '_em_sidebar_plans' ] as $k ) {
        register_post_meta( 'exercise', $k, [
            'type'              => 'string',
            'single'            => true,
            'show_in_rest'      => true,
            'auth_callback'     => $auth,
            'sanitize_callback' => function( $v ) {
                if ( is_array($v) ) return wp_json_encode($v);
                return (string) $v;
            },
        ]);
    }
}, 11 );
