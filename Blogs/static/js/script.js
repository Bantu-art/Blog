// Smooth scrolling for reply focus
$(document).on('click', '.reply-btn', function () {
    const commentId = $(this).data('comment-id');
    const form = $(this).closest('div').find('.comment-form');
    form.find('input[name="parent_id"]').val(commentId);
    form.find('textarea[name="content"]').focus();
    $('html, body').animate({
        scrollTop: form.offset().top - 100
    }, 500);
});

// Like button animation
$(document).on('click', '.like-btn', function () {
    const likeBtn = $(this);
    likeBtn.addClass('liked');
    setTimeout(() => likeBtn.removeClass('liked'), 300);
});