(function ($) {

    "use strict";

    var fullHeight = function () {

        $('.js-fullheight').css('height', $(window).height());
        $(window).resize(function () {
            $('.js-fullheight').css('height', $(window).height());
        });

    };
    fullHeight();

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

    $('#covid').DataTable({
        paging: false,
        fixedHeader: false,
        autoWidth: false,
        info: false,
        scrollX: '100%',
        responsive: false,
        scrollCollapse: true,
        language: {
            search: "Axtarış:",
            emptyTable: "Məlumat tapılmadı. Zəhmət olmasa az sonra yenidən yoxlayın.<br/>" +
                "Əgər yenə alınmasa mənə <a href=\"mailto:sh.maharramov@gmail.com?subject=Coronavirus - Məlumat tapılmadı\">Email</a> göndərin."
        },
        "createdRow": function (row, data, index) {
            if (data[2].replace(/[\$,]/g, '') * 1 > 0) {
                $('td', row).eq(2).addClass('highlight_maroon');
            }
            if (data[4].replace(/[\$,]/g, '') * 1 > 0) {
                $('td', row).eq(4).addClass('highlight_red');
            }
            if (data[1].indexOf('baijan') >= 0) {
                $('td', row).eq(0).addClass('bottom_red');
            }
        }
    });

})(jQuery);
