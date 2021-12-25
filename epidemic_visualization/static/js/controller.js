function gettime() {
	$.ajax({
		url: "/time",
		timeout: 10000, //超时时间设置为10秒；
		success: function(data) {
			$("#tim").html(data)
		},
		error: function(xhr, type, errorThrown) {

		}
	});
}

function get_c1_data() {
	$.ajax({
		url: "/c1",
		success: function(data) {
			$(".timer").eq(0).text(data.confirm);
			$(".timer").eq(1).text(data.heal);
			$(".timer").eq(2).text(data.dead);
			$(".timer").eq(3).text(data.motrality);
		},
		error: function(xhr, type, errorThrown) {

		}
	})
}

//function get_c2_data() {
//    $.ajax({
//        url:"/c2",
//        success: function(data) {
//			ec_center_option.series[0].data=data.data;
//            ec_center.setOption(ec_center_option)
//		},
//		error: function(xhr, type, errorThrown) {
//
//		}
//    })
//}

function get_world_c2_data() {
    $.ajax({
        url:"/world",
        success: function(data) {
			option.series[0].data=data.data;
            myChart.setOption(option)
		},
		error: function(xhr, type, errorThrown) {

		}
    })
}

function get_l1_data() {
    $.ajax({
        url:"/l1",
        success: function(data) {
            ec_left1_Option.series[0].data=data.data;
            ec_left1.setOption(ec_left1_Option)
		},
		error: function(xhr, type, errorThrown) {

		}
    })
}

function get_l2_data() {
    $.ajax({
        url:"/l2",
        success: function(data) {
			ec_left2_Option.xAxis[0].data=data.day;
            ec_left2_Option.series[0].data=data.local_add;
            ec_left2_Option.series[1].data=data.foreign_add;
            ec_left2.setOption(ec_left2_Option)
		},
		error: function(xhr, type, errorThrown) {

		}
    })
}

function get_r1_data() {
    $.ajax({
        url: "/top",
        success: function (data) {
            ec_right1_option.xAxis.data=data.nation;
            ec_right1_option.series[0].data=data.updates;
            ec_right1.setOption(ec_right1_option);
        }
    })
}

function get_r2_data() {
    $.ajax({
        url: "/r2",
        success: function (data) {
            ec_right2_option.series[0].data=data.kws;
            ec_right2.setOption(ec_right2_option);
        }
    })
}

function get_na_data() {
    $.ajax({
        url: "/aa",
        success: function (data) {
            console.log(data)
            option1.series[0].data=data.data;
            myChart1.setOption(option1)
        }
    })
}

function get_R2_world_data() {
    $.ajax({
        url: "/F2",
        success: function (data) {

            html = "<table width='100%' border='1' cellspacing='1' cellpadding='0' style='color:#ffffff'>"
            html += "<thead>" +
                         "<tr>" +
                             "<th>国家</th>" +
                             "<th>新增</th>" +
                             "<th>累计</th>" +
                             "<th>治愈</th>" +
                             "<th>死亡</th>" +
                         "</tr>" +
                    "</thead>"
            html += "<tbody>"
            for (var i = 0; i < 216; i++){
                html += "<tr>" +
                           "<td>" + data.province[i] + "</td>" +
                           "<td>" + data.newly[i] + "</td>" +
                           "<td>" + data.total[i] + "</td>" +
                           "<td>" + data.cured[i] + "</td>" +
                           "<td>" + data.death[i] + "</td>" +
                         "</tr>"
            }
            html += "</tbody></table>"
            document.getElementById("F2").innerHTML = html;
        }
    })
}

function get_home_data() {
        $.ajax({
        url: "/home_data",
        success: function (data) {
            console.log(data)
            html = ""
            for (var i = 0; i < 10; i++){
                if (i == 0){
                    html += "<li><a href='" + data.link[i] + "'>" + data.headline[i] +
                        "</a><img src='../static/images/ico_new.gif' width='21' height='10' />" + data.pubtime[i] + "</li>"
                }else {
                    html += "<li><a href='" + data.link[i] + "'>" + data.headline[i] + "</a>" + data.pubtime[i] + "</li>"
                }
            }

            document.getElementById("list_1").innerHTML = html;
        }
    })
}

function get_abroad_data() {
        $.ajax({
        url: "/abroad_data",
        success: function (data) {
            console.log(data)
            html = ""
            for (var i = 0; i < 10; i++){
                if (i == 0){
                    html += "<li><a href='" + data.link[i] + "'>" + data.headline[i] +
                        "</a><img src='../static/images/ico_new.gif' width='21' height='10' />" + data.pubtime[i] + "</li>"
                }else {
                    html += "<li><a href='" + data.link[i] + "'>" + data.headline[i] + "</a>" + data.pubtime[i] + "</li>"
                }
            }

            document.getElementById("list_2").innerHTML = html;
        }
    })
}

gettime();
get_c1_data();
//get_c2_data();
get_world_c2_data();
get_R2_world_data();
get_l1_data();
get_l2_data();
get_r1_data();
//get_r2_data();
get_na_data();
get_home_data();
get_abroad_data();
setInterval(gettime,1000);
setInterval(get_c1_data,1000*10);
//setInterval(get_c2_data,10000*10);
setInterval(get_world_c2_data,10000*10);
setInterval(get_l1_data,10000*10);
setInterval(get_l2_data,10000*10);
setInterval(get_r1_data,10000*10);

//setInterval(get_r2_data,10000*10);
