$(document).ready(function () {
    $('body').on('click', '.input', function (e) {
        $(this).blur(function () {

            t = this
            idn = t.id
            if (idn == 'user') {
                if (this.value == '') {
                    this.nextElementSibling.id = 'uid'
                    this.nextElementSibling.textContent = '用户名必填'
                }
                else {
                    var data = {data: JSON.stringify({'u': this.value, 'i': 'u'})}
                    $.ajax({
                        type: 'POST',
                        url: '/register',
                        data: data,
                        dataType: 'json',
                        success: function (data) {
                            console.log(data.msg)
                            t.nextElementSibling.id = 'uid'
                            t.nextElementSibling.textContent = data.msg
                        }
                    })
                }
            }
            else if (idn == 'email') {
                var reg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$");
                var obj = document.getElementById("email")
                if (obj.value === "") {
                    this.nextElementSibling.id = 'uid'
                    this.nextElementSibling.textContent = '邮箱必填'
                }
                else if (!reg.test(obj.value)) {
                    this.nextElementSibling.id = 'uid'
                    this.nextElementSibling.textContent = '邮箱格式错误'
                }
                else {
                    var data = {data: JSON.stringify({'u': this.value, 'i': 'e'})}
                    $.ajax({
                        type: 'POST',
                        url: '/register',
                        data: data,
                        dataType: 'json',
                        success: function (data) {
                            console.log(data.msg)
                            t.nextElementSibling.id = 'uid'
                            t.nextElementSibling.textContent = data.msg
                        }
                    })
                }
            }
            else if (idn == 'tel') {
                var data = {data: JSON.stringify({'u': this.value, 'i': 't'})}
                if (this.value != '') {
                    var myreg = /^[1][3,4,5,7,8][0-9]{9}$/;
                    if (!myreg.test(this.value)) {
                        this.nextElementSibling.id = 'uid'
                        this.nextElementSibling.textContent = '手机格式错误'
                    }
                    else {
                        $.ajax({
                            type: 'POST',
                            url: '/register',
                            data: data,
                            dataType: 'json',
                            success: function (data) {
                                console.log(data.msg)
                                t.nextElementSibling.id = 'uid'
                                t.nextElementSibling.textContent = data.msg
                            }
                        })

                    }

                }

            }
            else if (idn == 'pas2') {
                var pas1 = $('#pas1')[0].value
                if (t.value != pas1) {
                    this.nextElementSibling.id = 'uid'
                    this.nextElementSibling.textContent = '密码输入不一致'
                }
                else {
                    this.nextElementSibling.id = ''
                    this.nextElementSibling.textContent = '二次密码正确'

                }

            }
        })
    })   //注册输入框验证
    $('body').on('click', '#bt2', function (e) {

        info = new Array()
        t = $(this)
        $('.usg').each(function () {
            info.push($(this)[0].innerText)
        })
        flag = $.inArray('用户名可注册', info) != -1 ? $.inArray('二次密码正确', info) != -1 ? $.inArray('邮箱可注册', info) != -1 ? a(t, info) : '' : '' : ''
        if (flag == 1) {
            info = new Array()
            $('.input').slice(-5,).each(function () {
                info.push(this.value)
            })
            var data = {data: JSON.stringify({'info': info, 'success': 1})}
            $.ajax({
                type: 'POST',
                url: '/reg',
                data: data,
                dataType: 'json',
                success: function (data) {
                    window.u = data.u
                    if (data.msg == 'success') {
                        //定时跳转

                        setInterval(rer(), 3000);

                        function rer() {
                            window.location.href = 'http://' + window.location.host + '/' + data.relname + '?uid=' + data.uid;
                        }

                    }
                }
            })
        }
    })  //注册按钮验证
    if ($('.tab').prevObject[0].title == '注册异常') {
        $('.group').hide()
    }  // 定义昵称异常
    else {
        if (window.location.pathname == '/pickname') {
            $('.button').on('click', function () {
                pickname = $('.input')[0].value
                femail = $('input:radio[name="2"]:checked').val()

                data = {'pickname': pickname, 'sex': femail, 'u': document.cookie.split('=')[1]}
                $.ajax({
                    type: 'POST',
                    url: '/pickname',
                    data: data,
                    dataType: 'json',
                    success: function (data) {
                        window.location.href = 'http://' + window.location.host + '/'
                    }

                })
            })
        }
    }

    //登陆验证
    $('#bt1').click(function () {
        user = $('.input')[0].value
        pwd = $('.input')[1].value
        data = {'u': user, 'p': pwd},
        $.ajax({
            type: 'POST',
            url: '/login',
            data: data,
            dataType: 'json',
            success: function (data) {
                if (data.msg == '1') {
                    //定时跳转
                    setInterval(rer(), 3000);
                    function rer() {
                        window.location.href =  'http://' + window.location.host + '/';
                    }

                }
                else {
                     $('.hr').text('无效的用户名或密码')

                }
            }
        })
    })


})

function a(t, i) {
    return $.inArray('手机格式错误', i) == -1 ? 1 : -1
}

