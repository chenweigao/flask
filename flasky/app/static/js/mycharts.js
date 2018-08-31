// Javascript
let chart = new Chart( "#chart", { // or DOM element
  data: {
    labels: ["12am-3am", "3am-6am", "6am-9am", "9am-12pm",
    "12pm-3pm", "3pm-6pm", "6pm-9pm", "9pm-12am"],
  
    datasets: [
    {
      label: "Some Data", type: 'bar',
      values: [25, 40, 30, 35, 8, 52, 17, -4]
    },
    {
      label: "Another Set", type: 'bar',
      values: [25, 50, -10, 15, 18, 32, 27, 14]
    },
    {
      label: "Yet Another", type: 'line',
      values: [15, 20, -3, -15, 58, 12, -17, 37]
    }
    ],
  
    yMarkers: [{ label: "Marker", value: 70 }],
    yRegions: [{ label: "Region", start: -10, end: 50 }]
  },
  
  title: "My Awesome Chart",
  type: 'axis-mixed', // or 'bar', 'line', 'pie', 'percentage'
  height: 250,
  colors: ['purple', '#ffa3ef', 'red']
  });