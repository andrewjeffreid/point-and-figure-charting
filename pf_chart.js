// from API
const dailyHigh = [20,21,22,21,21,23]
const dailyLow = [19,20,18,17,20,15]
const stepSize = 1
const maxYVal = Math.max(...dailyHigh)
const minYVal = Math.min(...dailyLow)

// chart object
chart = {
    trend: null,
    price: null,
    stepSize: stepSize,
}
let yVals = []

//setup y-axis
yVals = []
for (var i = minYVal; i <= maxYVal; i += chart.stepSize) {
    yVals.push(i);
}
const reverseYVals = yVals.slice().reverse()

// grid 
const rows = []
yVals.forEach(yVal => rows.push(yVal.toString() + ","))
rows.reverse()

// new "x" column
const addXCol = (price) => {
    rows.forEach(row => {
        if (price === parseFloat(row.split(",")[0])) {
            rows[rows.indexOf(row)] += "x"
            chart.trend = "x"
            chart.price = parseFloat(row.split(",")[0])
        } else {
            rows[rows.indexOf(row)] += " "
        }
    })
}

// add "x" to existing column
const addX = (price) => {
    rows.forEach(row => {
        if (price === parseFloat(row.split(",")[0])) {
            rows[rows.indexOf(row)] = row.slice(0, -1) + "x"
            chart.trend = "x"
            chart.price = parseFloat(row.split(",")[0])
        }
    })
}

// new "o" column
const addOCol = (price) => {
    rows.forEach(row => {
        if (price === parseFloat(row.split(",")[0])) {
            rows[rows.indexOf(row)] += "o"
            chart.trend = "o"
            chart.price = parseFloat(row.split(",")[0])
        } else {
            rows[rows.indexOf(row)] += " "
        }
    })
}

// new "x" column
const addO = (price) => {
    rows.forEach(row => {
        if (price === parseFloat(row.split(",")[0])) {
            rows[rows.indexOf(row)] = row.slice(0, -1) + "o"
            chart.trend = "o"
            chart.price = parseFloat(row.split(",")[0])
        }
    })
}

// get values for rising action points
const getHighPrice = (dailyHigh) => {
    let highPrice
    let i = 0
    while (yVals[i] <= dailyHigh) {
        highPrice = yVals[i]
        i += 1
    }
    return highPrice
}

// get values for falling action points
const getLowPrice = (dailyLow) => {
    let lowPrice
    let i = 0
    while (reverseYVals[i] >= dailyLow) {
        lowPrice = reverseYVals[i]
        i += 1
    }
    return lowPrice
}

// charting algorithm
const action = (dailyHigh, dailyLow) => {

    // demand
    if (chart.trend === "x") {

        // establish action points
        const apHigh = yVals[yVals.indexOf(chart.price) + 1]
        const apLow = yVals[yVals.indexOf(chart.price) - 3]

        // check daily low, did it fall?
        if (dailyHigh >= apHigh) {

            // add appropriate x's
            yVals.slice(yVals.indexOf(apHigh), yVals.indexOf(getHighPrice(dailyHigh)) + 1).forEach(yVal => {
                addX(yVal)
            })

        } else {

            // 3 box reversal?
            if (dailyLow <= apLow) {

                // add new o column
                addOCol(apLow + 2)
                reverseYVals.slice(reverseYVals.indexOf(apLow) - 2, reverseYVals.indexOf(getLowPrice(dailyLow)) + 1).forEach(yVal => {
                    addO(yVal)
                })
            }
        }

    // supply
    } else if (chart.trend === "o") {
        
        // establish action points
        const apLow = yVals[yVals.indexOf(chart.price) - 1]
        const apHigh = yVals[yVals.indexOf(chart.price) + 3]

        // check daily low, did it fall?
        if (dailyLow <= apLow) {

            // add appropriate o's
            reverseYVals.slice(reverseYVals.indexOf(apLow) - 2, reverseYVals.indexOf(getLowPrice(dailyLow)) + 1).forEach(yVal => {
                addO(yVal)
            })

        } else {

            // 3 box reversal
            if (dailyHigh >= apHigh) {

                // add new x column
                addXCol(apHigh - 2)
                yVals.slice(yVals.indexOf(apHigh) - 1, yVals.indexOf(getHighPrice(dailyHigh)) + 1).forEach(yVal => {
                    addX(yVal)
                })

            }
        }

    // new graph
    } else {

        addXCol(getHighPrice(dailyHigh))

    }
}

// generate chart
for (i=0; i <= dailyHigh.length; i++ ) {
    action(dailyHigh[i], dailyLow[i])
}

//rows.forEach(row => console.log(row[row.length-1]))
rows.forEach(row => console.log(row))