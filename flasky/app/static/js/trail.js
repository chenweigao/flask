var myChart = echarts.init(document.getElementById('main'), 'vintage');
//var data_original = document.getElementById('data').value;
var data_array_x = new Array();
var data_array_y = new Array();
//var data_modify = data_original.split(" ")

// console.log(data_original);

// var jsonData = JSON.parse(data_original.replace(/ObjectId\(/g, '').replace(/\)/g, '').replace(/'/g, '"'))


var xhr = new XMLHttpRequest();
xhr.open('GET', '/data.json', true);
xhr.onreadystatechange = function () {
    // readyState == 4说明请求已完成
    if (xhr.readyState == 4 && xhr.status == 200 || xhr.status == 304) {
        // 从服务器获得数据 
        //fn.call(this, xhr.responseText);
        console.log(this.responseText);
        var jsonData = JSON.parse(xhr.responseText.replace(/'/g, '"'));


        // for (var i = 3, j = 0; i < data_modify.length; i += 9, j++) {
        //     data_array_x[j] = Number(data_modify[i].slice(0, data_modify[i].length - 1))
        //     data_array_y[j] = Number(data_modify[i + 2].slice(0, data_modify[i + 2].length - 1))

        // }

        for (let i = 0; i < jsonData.length; i++) {
            data_array_x[i] = jsonData[i].x;
            data_array_y[i] = jsonData[i].y;
        }

        var option = {
            xAxis: {
                // splitLine: {
                //     show: false
                // },
                axisLine: {
                    lineStyle: {
                        type: 'solid',
                        color: '#fff', //左边线的颜色
                        width: '2' //坐标线的宽度
                    }
                },
                data: data_array_x
            },
            yAxis: {
                // splitLine: {
                //     show: false
                // },
                axisLine: {
                    lineStyle: {
                        type: 'solid',
                        color: '#fff', //左边线的颜色
                        width: '2' //坐标线的宽度
                    }
                },

            },
            series: [{
                type: 'line',
                data: data_array_y
            }],
            dataZoom: [{
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
            //backgroundColor: 'rgba(255, 128, 128, 64)'
        };
        myChart.setOption(option);


    }
};
xhr.send();
//var bg=document.getElementById('background');

//bg.setAttribute('style','background: url(\'image/path.png\');width: 600px;height:400px');