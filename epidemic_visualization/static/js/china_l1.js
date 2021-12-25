//地理坐标图
    var geoCoordMap = {
    '珠海市': [113.353986,21.924979]
    ,'广州市':[113.480637,23.125178]
    ,'湛江市':[110.264977,21.274898]
    ,'茂名市':[110.919229,21.659751]
    ,'阳江市':[111.825107,21.859222]
    ,'云浮市':[112.044439,22.629801]
    ,'肇庆市':[112.472529,23.051546]
    ,'江门市':[112.894942,22.090431]
    ,'中山市':[113.382391,22.321113]
    ,'佛山市':[113.022717,22.828762]
    ,'清远市':[113.051227,23.685022]
    ,'韶关市':[113.591544,24.501322]
    ,'河源市':[114.897802,23.746266]
    ,'梅州市':[116.117582,24.099112]
    ,'潮州市':[116.692301,23.661701]
    ,'揭阳市':[116.255733,23.143778]
    ,'汕头市':[116.708463,22.87102]
    ,'汕尾市':[115.364238,22.774485]
    ,'深圳市':[114.085947,22.347]
    ,'东莞市':[113.746262,22.746237]
    ,'惠州市':[114.412599,23.079404]
    };

    var mydata = [
    {name: '珠海市',value:250973},
    {name: '广州市',value: 453088},
    {name: '中山市',value:424302},
    {name: '佛山市',value: 1135329},
    {name: '揭阳市',value:30035},
    {name: '梅州市',value: 47148},
    {name: '汕头市',value:65920},
    {name: '东莞市',value: 428881},
    {name: '惠州市',value:300025},
    {name: '汕尾市',value: 20154},
    {name: '江门市',value: 231140},
    {name: '清远市',value: 136351},
    {name: '肇庆市',value: 126912},
    {name: '河源市',value: 37704},
    {name: '韶关市',value: 44550},
    {name: '云浮市',value: 31672},
    {name: '潮州市',value: 26802},
    {name: '阳江市',value: 3114},
    {name: '茂名市',value: 39238},
    {name: '湛江市',value: 48422},
    ];

// 初始化echarts示例mapChart
var mapChart = echarts.init(document.getElementById('l1_c'), "dark");

// mapChart的配置
var option = {
    title:{
        text:'广东省各地市累计确诊',
        x:'center',
    },
    tooltip:{
        trigger:'item'
    },
    series: [{
        name: '累计确诊', // series名称
        type: 'map', // series图表类型
        map: '广东',
        coordinateSystem: 'geo', // series坐标系类型
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
        data:mydata // series数据内容
    }],
    visualMap: {
        min: 0,
        max: 10000,
        left: 'left',
        top: 'bottom',
        realtime: false,
        calculable: true,
        inRange:{
            color: ['lightskyblue', 'yellow', 'orangered']
        }
    }
};
mapChart.setOption(option);