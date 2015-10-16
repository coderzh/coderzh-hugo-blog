(function (w) {
    var $ = w.jQuery,
        done = false,
        ready = function () {
            $('form.searchform').on('submit', function (event) {
                if (false === done) {
                    event.preventDefault();
                    var target = event.currentTarget || event.target;
                    var $form = w.jQuery(target);
                    var orgVal = $form.find('.search').val();
                    $form.find('.search').val('site:blog.coderzh.com/ ' + orgVal);
                    done = true;
                    $form.submit();
                }
            });
            $('.hubinfo').each(function (i, e) {
                var $elem = $(e);
                $elem.hubInfo({
                    user : $elem.data('u') || 'coderzh',
                    repo : $elem.data('r') || ''
                });
            });
            $('.hentry').matchHeight();
            $('.related.post-hover').matchHeight();
        },
        hasSetBg = false,
        scroller = function (event) {
            var target = event.srcElement || event.target;
            if (target.body.scrollTop > 10 && false === hasSetBg) {
                $('.nav-container').css({
                    background : '#26272b'
                });
                $('.nav-cs-icon').show();
                hasSetBg = true;
            }
            if (0 === target.body.scrollTop && true === hasSetBg) {
                $('.nav-container').css({
                    background : 'none'
                });
                $('.nav-cs-icon').hide();
                hasSetBg = false;
            }
        };

    if (window.addEventListener) {
        window.addEventListener('load', ready, false);
        window.addEventListener('scroll', scroller, false);
    } else {
        if (window.attachEvent) {
            window.attachEvent('onload', ready);
            window.attachEvent('onscroll', scroller);
        }
    }
    w.hljs.initHighlightingOnLoad();
})(window);
