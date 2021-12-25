var ec_right1_c = echarts.init(document.getElementById('r1_c'),"dark");
var ec_right1_option_c = {
    backgroundColor: '#222222',
	//标题样式
	title : {
	    text : "今日新增省级TOP10",
	    textStyle : {
	        color : '#7171C6',
	    },
	    left : 'center'
	},



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
		barMaxWidth:"30%",
		itemStyle: {
            normal: {
　　　　　　　　//这里是重点
                color: function(params) {
                	//注意，如果颜色太少的话，后面颜色不会自动循环，最好多定义几个颜色
                    var colorList = ['red', '#D94600', '#F75000', '#FF5809', '#FF8040', '#FF8F59', '#FF9D6F', '#FFAD86', '#FFBD9D', '#FFE6D9'];
                    return colorList[params.dataIndex]
                }
            }
        }
    }]
};
ec_right1_c.setOption(ec_right1_option_c);