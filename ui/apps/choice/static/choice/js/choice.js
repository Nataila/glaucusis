$(document).ready(function () {
  //$('.stock-list li ul').hide();
  ////不包含子菜单时鼠标指针和项目图标
  //$('.stock-list li:not(:has(ul))').css({ 'cursor': 'default', 'list-style-image': 'none' });
  ////包含子菜单时鼠标指针和项目图标
  //$('.stock-list li:has(ul)').css({ 'cursor': 'pointer', 'list-style-image': 'url(../static/choice/images/plus.gif)' });
  //$('.stock-list li:has(ul)').click(function (event) {
  //  if (this == event.target) {
  //    $(this).css('list-style-image', ($(this).children().is(':hidden') ? 'url(../static/choice/images/minus.gif)' : 'url(../static/choice/images/plus.gif)'));
  //    $(this).children().slideToggle('normal');
  //  }
  //})
  $(".topnav").accordion({
    accordion:false,
    speed: 500,
    closedSign: '[+]',
    openedSign: '[-]'
  });
})
