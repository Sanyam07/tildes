// Copyright (c) 2018 Tildes contributors <code@tildes.net>
// SPDX-License-Identifier: AGPL-3.0-or-later

$.onmount('[data-js-markdown-edit-tab]', function() {
    $(this).click(function(event) {
        var $editTextarea = $(this).closest('form').find('[name="markdown"]');
        var $previewDiv = $(this).closest('form').find('[data-js-markdown-preview]');

        $editTextarea.removeClass('d-none');
        $previewDiv.addClass('d-none');
    });
});
