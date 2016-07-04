/**
 * Created by benma_000 on 13/04/2016.
 */

var main = function() {
    var current = $('.dropdown');
    var menu = $('.dropdown-content');

    current.click( function() {
        menu.slideToggle();
    });
};

$(document).ready(main);