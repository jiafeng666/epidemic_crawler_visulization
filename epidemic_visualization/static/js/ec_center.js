var ec_center = echarts.init(document.getElementById('c2'), "dark");

var mydata = [{'name': '上海', 'value': 318}, {'name': '云南', 'value': 162}];

var ec_center_option = {
    backgroundColor: '#222222',
    title: {

        text: '全国疫情实况追踪',
        subtext: '',
        x: 'center',
        textStyle:{
            fontSize: 35,
            color:'#009fe8'
            }
    },
    tooltip: {
        trigger: 'item'
    },
    //左侧小导航图标
    visualMap: {
        show: true,
        x: 'left',
        y: 'bottom',
        textStyle: {
            fontSize: 12,
        },
        splitList: [{ start: 0, end: 1},
            { start: 2,end: 99 },
            {start: 100, end: 999 },
			{ start: 1000, end: 9999 },
            {  start: 10000, end: 99999 },
            { start: 100000 }],
        color: ['#8A3310', '#C64918', '#E55B25', '#F2AD92', '#F9DCD1', '#ffffff']
    },
    //配置属性
    series: [{
        name: '现有确诊',
        type: 'map',
        mapType: 'china',
        roam: false, //拖动和缩放
        itemStyle: {
            normal: {
                borderWidth: .5, //区域边框宽度
                borderColor: '#009fe8', //区域边框颜色
                areaColor: "#ffefd5", //区域颜色
            },
            emphasis: { //鼠标滑过地图高亮的相关设置
                borderWidth: .5,
                borderColor: '#4b0082',
                areaColor: "#fff",
            }
        },
        label: {
            normal: {
                show: true, //省份名称
                fontSize: 8,
            },
            emphasis: {
                show: true,
                fontSize: 8,
            }
        },
        data: [] //mydata //数据
    }]
};
ec_center.setOption(ec_center_option);