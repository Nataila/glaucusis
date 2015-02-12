$(document).ready(function () {
  $('.add-list-ok').on('click', function () {
    var watched_name = $('[name=watched_name]').val();
    var nowHref = window.location.href;
    $.getJSON('/stock/add_watch_list', {'watched_name': watched_name}, function(data) {
      if (data === 200){
        window.location.href=nowHref;
      }
    })
  })

  $('.add-news-list-ok').on('click', function () {
    var name = $('[name=watched_list_name]').val();
    $.getJSON('/news/set_news_list', {'name': name}, function (data) {
      if (data=200) {
        window.location.href='/news';
      }
    })
  })
  var getNewsRemind = function () {
    $.getJSON('/news/news_remind', function (data) {
      if (data.count > 0) {
        $('.badge-news-remind').text(data.count);
      }
    })
  }
  getNewsRemind();
  setInterval(getNewsRemind, 6000);
  $('#news-remind').on('click', function () {
    var count = $('.badge-news-remind:eq(0)').text();
    window.location.href = '/set_account/?news='+count;
  })
})
