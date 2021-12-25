    // 基于准备好的dom，初始化echarts实例
    var myChart1 = echarts.init(document.getElementById('aa'));

    option1 = {
          tooltip: {
            trigger: 'item'

          },
          legend: {
            top: '1%',
            left: 'center',
            textStyle: {
            color: "#339999", // 文字的颜色。

            fontWeight: "normal", // 文字字体的粗细。 'normal' 'bold'  'bolder' 'lighter'  100 | 200 | 300 | 400...

            fontSize: 20, // 文字的字体大小。
            }
          },
          series: [
            {
              name: '各大洲比例',
              type: 'pie',
              radius: ['40%', '70%'],
              avoidLabelOverlap: false,
              itemStyle: {
                borderRadius: 10,
                borderColor: '#fff',
                borderWidth: 2,
              },
              label: {
                show: false,
                position: 'center'
              },
              emphasis: {
                label: {
                  show: true,
                  fontSize: '40',
                  fontWeight: 'bold'
                }
              },
              labelLine: {
                show: false
              },
              data: []
            }
          ]
        };
    // 使用刚指定的配置项和数据显示图表。
    myChart1.setOption(option1);