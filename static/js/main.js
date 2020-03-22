(function ($) {

    "use strict";

    const fullHeight = function () {

        $('.js-fullheight').css('height', $(window).height());
        $(window).resize(function () {
            $('.js-fullheight').css('height', $(window).height());
        });

    };

    fullHeight();

    const table = $('#covid').DataTable({
        paging: false,
        //fixedHeader: false,
       // autoWidth: false,
        info: false,
        scrollX: true,
        //responsive: true,
        scrollCollapse: false,
        language: {
            search: "Axtarış:",
            emptyTable: "Məlumat tapılmadı. Zəhmət olmasa az sonra yenidən yoxlayın.<br/>" +
                "Əgər yenə alınmasa mənə <a href=\"mailto:sh.maharramov@gmail.com?subject=Coronavirus - Məlumat tapılmadı\">Email</a> göndərin."
        },
        "createdRow": function (row, data, index) {
            if (data[2].replace(/[$,]/g, '') * 1 > 0) {
                $('td', row).eq(2).addClass('highlight_maroon');
            }
            if (data[4].replace(/[$,]/g, '') * 1 > 0) {
                $('td', row).eq(4).addClass('highlight_red');
            }
            if (data[0].indexOf('baijan') >= 0) {
                $('td', row).eq(0).addClass('bottom_red');
            }
        }
    });

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $($.fn.dataTable.tables(true)).DataTable().columns.adjust().responsive.recalc();
    });


})(jQuery);
