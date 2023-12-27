const arr = [0,1,2,3,4]

const it = arr[Symbol.iterator]()


// val = it.next()
// while (!val.done) {
//     console.log(val.value)
//     val = it.next()
// }

for (let x of it) {
    console.log(x)
}