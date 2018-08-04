
$(document).ready(function() { 

    
    
    let myChart = document.getElementById('myChart').getContext('2d');

    var entropy = Number($('#entropy').text());
    var avgLen = Number($('#avg').text());
    var uppere = entropy + 1;

    let entropyChart = new Chart(myChart, {

        type: 'bar',
        data: {

            labels: ['Entropy Lower', 'Average Code Length', 'Entropy Upper'],
            datasets: [{

                label: ['U','Avg', 'L'],
                data: [entropy, avgLen, uppere],
                backgroundColor: ['#9fa0ff','#8895b3', '#dab6fc'],
                borderWidth: 1,
                borderColor: '#000'
            
            }],
            
        },
        options: {
            legend: { display: false },
            title: {
              display: true,
              text: 'Entropy Bounds'
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
        }

        }
            
    });


    let myTimes = document.getElementById('myTimes').getContext('2d');

    var bintime = Number($('#timebin').text());
    var vebtime = Number($('#timeveb').text());
    var yfasttime = Number($('#timeyfast').text());

    console.log(bintime, vebtime, yfasttime);

    let myTimesChart = new Chart(myTimes, {

        type: 'bar',
        data: {

            labels: ['Binary Heap', 'van Emde Boas', 'y-Fast Trie'],
            datasets: [{

                label: ['Bin','vEB', 'y-Fast'],
                data: [bintime, vebtime, yfasttime],
                backgroundColor: ['#9fa0ff','#8895b3', '#dab6fc'],
                borderWidth: 1,
                borderColor: '#000'
            
            }],
            
        },
        options: {
            legend: { display: false },
            title: {
              display: true,
              text: 'Times (ms)'
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
        }

        }
            
    });



    var huff = $('#demo').drawsvg({duration: 5000,});
    huff.drawsvg('animate');

});
