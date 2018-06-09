/**
 * Created by hynev on 2017/10/7.
 */
$(function () {
   var wrap = document.getElementById("wrap");
var imgs = document.getElementById("imgs").getElementsByTagName("a");
var paging = document.getElementById("paging").getElementsByTagName("span");
var btn = document.getElementById("btn").getElementsByTagName("li");
var timer = 0;
var index = 0;

imgs[0].style.display = "block";
btn[0].className = "on";

// 点击
for (var i=0; i<btn.length; i++) {
    btn[i].index = i;
    btn[i].onclick = function() {
        var that = this;
        checkout(function() {
            index = that.index;
        });
    };

    // 禁止拖拽图片
    imgs[i].ondrag = imgs[i].onmousedown = function(e) {
        e = e || event;
        e.preventDefault ? e.preventDefault() : window.event.returnValue = false;
    }
}

for (var i=0; i<paging.length; i++) {
    // 下一张
    if (i) {
        paging[i].onclick = function() {
            checkout(function() {
                index++;
                index = index%imgs.length;
            });
        }

    // 上一张
    } else {
        paging[i].onclick = function() {
            checkout(function() {
                index--;
                if (index<0) index = imgs.length-1;
            });
        }
    }
}

function checkout(callback) {
    btn[index].className = "";
    imgs[index].style.display = "none";
    callback && callback();
    btn[index].className = "on";
    imgs[index].style.display = "block";

}

function auto() {
    timer = setInterval(function() {
        checkout(function() {
            index++;
            index = index%imgs.length;
        });
    }, 5000);
}

auto();

wrap.onmouseover = function() {
    clearInterval(timer);
}
wrap.onmouseout = function() {
    auto();
}
});