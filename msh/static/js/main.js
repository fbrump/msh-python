jQuery(document).ready(function($) {
    // DATE PICKER
    $.fn.datepicker.defaults.format = "yyyy-mm-dd";
    $('.content-date .input-group.date').datepicker({
        calendarWeeks: true,
        autoclose: true,
        todayHighlight: true,
        beforeShowYear: function (date){
                      if (date.getFullYear() == 2007) {
                        return false;
                      }
                    },
        toggleActive: true
    });

    // TIME PICKER
    $('.content-time .input-group.time').clockpicker({
        placement: 'botton',
        align: 'left',
        //donetext: 'Done',
        autoclose: true,
        'default': 'now'
    });
});