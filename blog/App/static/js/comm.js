$(document).ready(function () {
    //nav


    var obj = null;
    var As = document.getElementById('starlist').getElementsByTagName('a');
    obj = As[0];
    for (i = 1; i < As.length; i++) {
        if (window.location.href.indexOf(As[i].href) >= 0) obj = As[i];
    }
    obj.id = 'selected';
    //nav
    $("#mnavh").click(function () {
        $("#starlist").toggle();
        $("#mnavh").toggleClass("open");
    });
    //search  
    $(".searchico").click(function () {
        $(".search").toggleClass("open");
    });
    //searchclose 
    $(".searchclose").click(function () {
        $(".search").removeClass("open");
    });
    //banner
    $('#banner').easyFader();
    //nav menu   
    $(".menu").click(function (event) {
        $(this).children('.sub').slideToggle();
    });
    //tab
    $('.tab_buttons li').click(function () {
        $(this).addClass('newscurrent').siblings().removeClass('newscurrent');
        $('.newstab>div:eq(' + $(this).index() + ')').show().siblings().hide();
    });
    // 底部加载统计
    pycs = $('.blogtitle').length;
    totals = $('.load_btn')[0].innerText.replace(/[^0-9]/ig, "");
    if (pycs == totals) {
        loadbtninfo()
    }
    // 滑动加载
    // //文档高度
    // function getDocumentTop() {
    //     var scrollTop = 0, bodyScrollTop = 0, documentScrollTop = 0;
    //     if (document.body) {
    //         bodyScrollTop = document.body.scrollTop;
    //     }
    //     if (document.documentElement) {
    //         documentScrollTop = document.documentElement.scrollTop;
    //     }
    //     scrollTop = (bodyScrollTop - documentScrollTop > 0) ? bodyScrollTop : documentScrollTop;
    //     return scrollTop;
    // }

    //可视窗口高度
    // function getWindowHeight() {
    //     var windowHeight = 0;
    //     if (document.compatMode == "CSS1Compat") {
    //         windowHeight = document.documentElement.clientHeight;
    //     } else {
    //         windowHeight = document.body.clientHeight;
    //     }
    //     return windowHeight;
    // }

    // //滚动条滚动高度
    // function getScrollHeight() {
    //     var scrollHeight = 0, bodyScrollHeight = 0, documentScrollHeight = 0;
    //     if (document.body) {
    //         bodyScrollHeight = document.body.scrollHeight;
    //     }
    //
    //     if (document.documentElement) {
    //         documentScrollHeight = document.documentElement.scrollHeight;
    //     }
    //     scrollHeight = (bodyScrollHeight - documentScrollHeight > 0) ? bodyScrollHeight : documentScrollHeight;
    //     return scrollHeight;
    // }

    $('.load_btn').click(function () {
        url = window.location.href;
        pycounts = $('.blogtitle').length;
        lid = $('.blogtitle')[$('.blogtitle').length - 1].innerText;
        counts = $('.load_btn')[0].innerText.replace(/[^0-9]/ig, "");
        if (pycounts >= counts) {
            loadbtninfo()
        }
        else {
            $.get(
                url,
                {
                    'timestamp': parseInt(new Date().getTime() / 1000),
                    'path': window.location.pathname,
                    'arg': window.location.search,
                    'length': counts,
                    'lid': lid
                },
                function (data) {
                    // dosomething
                    art = data['art'];
                    con = '';
                    for (var i = 0; i < art.length; i++) {
                        title1 = art[i]['title']
                        cate1 = art[i]['cate']
                        pic1 = art[i]['pic']
                        des1 = art[i]['des']
                        cid1 = art[i]['cid']
                        ctime = art[i]['create_time']

                        var conli = '<li>\n' +
                            '          <h3 class="blogtitle"><a href="/" target="_blank">' + title1 + '</a></h3>\n' +
                            '          <span class="blogpic imgscale"><i><span><a href="/">' + cate1 + '</a></span></i><a href="/" title=""><img src="' + /static/ + pic1 + '" alt=""></a></span>\n' +
                            '          <p class="blogtext">' + des1 + '</p>\n' +
                            '            <p class="bloginfo"><span>' + ctime + '</span><span>【<a href="/">' + cate1 + '</a>】</span></p>\n' +
                            '          <a href="/" class="viewmore">阅读更多</a> \n' +
                            '        </li>';
                        con += conli;
                    }
                    ;
                    $('.bloglist ul').append(con)
                    artcounts = art.length + pycounts
                    if (artcounts >= counts) {
                        loadbtninfo()
                    }
                }
            );
        }

    })

    function loadbtninfo() {
        $('.load_btn')[0].innerText = '已经到我的底线了，没有更多内容。。'
    }

});