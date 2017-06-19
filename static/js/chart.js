window.addEventListener( 'load', function () {
    console.log('1111')
    var urlData = '/data/2011.csv'
    d3.csv( urlData, function (error, testData) {
        console.log('222')
        console.log(testData[4])
    })
    
});