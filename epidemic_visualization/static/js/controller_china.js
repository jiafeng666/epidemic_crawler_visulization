function gettime() {
	$.ajax({
		url: "/time",
		timeout: 10000, //超时时间设置为10秒；
		success: function(data) {
			$("#tim1").html(data)
		},
		error: function(xhr, type, errorThrown) {

		}
	});
}

function get_c1_data() {
	$.ajax({
		url: "/china_c1",
		success: function(data) {
			$(".xyg").eq(0).text(data.confirm);
			$(".xyg").eq(1).text(data.symptom);
			$(".xyg").eq(2).text(data.suspected);
			$(".xyg").eq(3).text(data.overseas);
		},
		error: function(xhr, type, errorThrown) {

		}
	})
}

function get_c2_data() {
    $.ajax({
        url:"/c2",
        success: function(data) {
			ec_center_option.series[0].data=data.data;
            ec_center.setOption(ec_center_option)
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

function get_l2_china_data() {
    $.ajax({
        url:"/china_l2",
        success: function(data) {
			ec_left2_Option_c.xAxis[0].data=data.day;
            ec_left2_Option_c.series[0].data=data.local_add;
            ec_left2_Option_c.series[1].data=data.input_add;
            ec_left2_c.setOption(ec_left2_Option_c)
		},
		error: function(xhr, type, errorThrown) {

		}
    })
}

function get_r1_data() {
    $.ajax({
        url: "/china_r1",
        success: function (data) {
            ec_right1_option_c.xAxis.data=data.province;
            ec_right1_option_c.series[0].data=data.confirm;
            ec_right1_c.setOption(ec_right1_option_c);
        }
    })
}

function get_r2_china_data() {
    $.ajax({
        url: "/r2",
        success: function (data) {
            console.log(data)
            html = "<table width='100%' border='1' cellspacing='1' cellpadding='0' style='color:#ffffff'>"
            html += "<thead>" +
                         "<tr>" +
                             "<th>地区</th>" +
                             "<th>新增</th>" +
                             "<th>现有</th>" +
                             "<th>累计</th>" +
                             "<th>治愈</th>" +
                             "<th>死亡</th>" +
                         "</tr>" +
                    "</thead>"
            html += "<tbody>"
            for (var i = 0; i < 34; i++){
                html += "<tr>" +
                           "<td>" + data.province[i] + "</td>" +
                           "<td>" + data.newly[i] + "</td>" +
                           "<td>" + data.now[i] + "</td>" +
                           "<td>" + data.total[i] + "</td>" +
                           "<td>" + data.cured[i] + "</td>" +
                           "<td>" + data.death[i] + "</td>" +
                         "</tr>"
            }
            html += "</tbody></table>"
            document.getElementById("r2").innerHTML = html;
        }
    })
}

gettime();
get_c1_data();
get_c2_data();
get_l2_china_data();
get_r1_data();
get_r2_china_data();

setInterval(gettime,1000);
setInterval(get_c1_data,1000*10);
setInterval(get_c2_data,10000*10);
setInterval(get_l2_china_data,10000*10);
setInterval(get_r1_data,10000*10);
setInterval(get_r2_china_data,10000*10);