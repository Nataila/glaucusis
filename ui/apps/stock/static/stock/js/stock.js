$(document).ready(function () {
  $('#exchange').find('.panel-collapse:eq(0)').addClass('in');
  var get_news = function (instrId) {
    $.getJSON('get_news', {'instrId': instrId}, function (data) {
      console.log($('#tplNews'))
      var $tpl = $('#tplNews').html();
      $("#news-content").html(_.template($tpl, {'data': data}));
      $("#news-accordion").find('.panel-collapse:eq(0)').addClass('in');
      $('.new_link').on('click', function () {
        var toLink = $(this).data('link');
        window.open(toLink);
      })
    })
  }

  var instrId = $('[name=instr_id]').val();
  get_news(instrId);

  //$('.instrument-name').on('click', function () {
  //  var instrIds = $(this).find('a').data('id');
  //  get_news(instrIds);
  //})
})
