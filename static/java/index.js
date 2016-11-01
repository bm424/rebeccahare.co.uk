/**
 * Created by benma_000 on 01/11/2016.
 */

var main = function() {
    var menu = $('header');
    var menuwidth = menu.outerWidth().toString();
    var out = {left: '-='.concat(menuwidth, 'px')};
    var back = {left: '+='.concat(menuwidth, 'px')};
    $('main').animate(back, 500);
    $('div.photo').animate(back, 500);
    $('button.c-hamburger').click(function () {
        if ($(this).hasClass('is-active')) {
            $(this).removeClass('is-active');
            $(this).animate(out, 500);
            $('header').animate(out, 500);
            $('main').animate(out, 500);
            $('div.photo').animate(out, 500);

        } else {
            $(this).addClass('is-active');
            $(this).animate(back, 500);
            $('header').animate(back, 500);
            $('main').animate(back, 500);
            $('div.photo').animate(back, 500);
            }
        });
    };

$(document).ready(main);