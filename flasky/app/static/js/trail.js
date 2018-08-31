
var myChart = echarts.init(document.getElementById('main'),'vintage');
var data_original=document.getElementById('data').value;
var data_array_x=new Array();
var data_array_y=new Array();
var data_modify=data_original.split(" ")

for(var i=3,j=0;i<data_modify.length;i+=9,j++){
    data_array_x[j]=Number(data_modify[i].slice(0,data_modify[i].length-1))
    data_array_y[j]=Number(data_modify[i+2].slice(0,data_modify[i+2].length-1))
    
}

var option={
    xAxis:{
        splitLine:{show: false},
        axisLine: {
            lineStyle: {
                type: 'solid',
                color: '#fff',//左边线的颜色
                width:'2'//坐标线的宽度
            }
        },
        data:data_array_x
    },
    yAxis:{
        splitLine:{show: false},
        axisLine: {
            lineStyle: {
                type: 'solid',
                color: '#fff',//左边线的颜色
                width:'2'//坐标线的宽度
            }
        },

    },
    series:[
        {
            type:'line',
            data:data_array_y
        }
    ],
    dataZoom: [
        {
            type: 'slider',
            xAxisIndex: 0,
            start: 10,
            end: 60
        },
        {
            type: 'inside',
            xAxisIndex: 0,
            start: 10,
            end: 60
        },
        {
            type: 'slider',
            yAxisIndex: 0,
            start: 30,
            end: 80
        },
        {
            type: 'inside',
            yAxisIndex: 0,
            start: 30,
            end: 80
        }
    ],
    backgroundColor: 'rgba(128, 128, 128, 0)'
};
myChart.setOption(option);
//var bg=document.getElementById('background');

//bg.setAttribute('style','background: url(\'image/path.png\');width: 600px;height:400px');