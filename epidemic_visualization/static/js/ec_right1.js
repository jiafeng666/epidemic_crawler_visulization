var ec_right1 = echarts.init(document.getElementById('r1'),"dark");
var ec_right1_option = {
    backgroundColor: '#222222',
	//标题样式
	title : {
	    text : "今日新增TOP10",
	    textStyle : {
	        fontSize: 25,
	        color : '#009fe8',
	    },
	    left : 'center',
	},
	  color: ['red'],
	    tooltip: {
	        trigger: 'axis',
	        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
	            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
	        }
	    },
    xAxis: {
        type: 'category',
        data: []
    },
    yAxis: {
        type: 'value',
        axisLabel: {
            fontSize:10
        },
    },
    series: [{
        data: [],
        type: 'bar',
		barMaxWidth:"50%"
    }]
};
ec_right1.setOption(ec_right1_option);