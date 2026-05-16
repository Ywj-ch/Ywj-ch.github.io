/**
 * 浏览器标题动画
 * 功能：离开页面时显示"网络断开"，返回时显示"网络恢复"
 */

var OriginTitile = document.title;
var titleTime;
document.addEventListener("visibilitychange", function () {
  if (document.hidden) {
    document.title = "💻 网络断开，别走！";
    clearTimeout(titleTime);
  } else {
    document.title = "🌐 重新连接，网络恢复！";
    titleTime = setTimeout(function () {
      document.title = OriginTitile;
    }, 2000);
  }
});
