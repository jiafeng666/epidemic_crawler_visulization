var ec_left1 = echarts.init(document.getElementById('l1'), "dark");

var ec_left1_Option = {
    backgroundColor: '#222222',
	//标题样式
	title: {
		text: "全球累计确诊top10",
		textStyle: {
			color:'#009fe8',
			fontSize: 25,
		},
		left: 'center',
	},
	tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b} : {c} ({d}%)',

	},
	legend: {
		left: "right",
		data: [],

	},
	series: [
    {
      name: '累计确诊',
      type: 'pie',
      radius: [20, 180],
      center: ['50%', '50%'],
      roseType: 'radius',
      itemStyle: {
        borderRadius: 5,

      },
      label: {
        show: false,
        textStyle: {
		    fontSize:20,

		  }
      },
      emphasis: {
        label: {
          show: true
        }
      },
      data: []
      }
     ]
};

ec_left1.setOption(ec_left1_Option);
