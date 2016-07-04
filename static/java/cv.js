/**
 * Created by benma_000 on 14/03/2016.
 */


var main = function() {

    var current = $('.dropdown');
    var menu = $('.dropdown-content');

    var theatre_select = $('li.theatre');
    var skills_select = $('li.skills');
    var education_select = $('li.education');
    var bio_select = $('li.bio');

    var theatre_content = $('div.theatre');
    var skills_content = $('div.skills');
    var education_content = $('div.education');
    var bio_content = $('div.bio');

    theatre_content.hide();
    skills_content.hide();
    education_content.hide();
    bio_content.show();

    current.click( function() {
        menu.slideToggle();
    });

    theatre_select.click( function() {
        theatre_content.show();
        skills_content.hide();
        education_content.hide();
        bio_content.hide();
        current.text("Theatre Credits \u25bc");
        menu.slideToggle();
    });

    skills_select.click( function() {
        theatre_content.hide();
        skills_content.show();
        education_content.hide();
        bio_content.hide();
        current.text("Skills \u25bc");
        menu.slideToggle();
    });

    education_select.click( function() {
        theatre_content.hide();
        skills_content.hide();
        education_content.show();
        bio_content.hide();
        current.text("Training \u25bc");
        menu.slideToggle();
    });

    bio_select.click( function() {
        theatre_content.hide();
        skills_content.hide();
        education_content.hide();
        bio_content.show();
        current.text("Bio \u25bc");
        menu.slideToggle();
    });

};

$(document).ready(main);