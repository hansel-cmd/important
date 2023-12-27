const { default: axios } = require('axios')

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
    prompt: 'enter command > '
})

readline.prompt()
readline.on('line', async line => {
    switch (line) {
        case 'list keto foods':
            {
                const res = await axios.get('http://localhost:3001/food')
                function *showKetos() {
                    let ketosOnly = res.data.filter(item => item.dietary_preferences.includes('keto'))
                    for (ketos of ketosOnly) {
                        yield ketos
                    }
                }

                for (ketos of showKetos()) {
                    console.log(ketos.name)
                }

                readline.prompt()
            }
            break;
        case 'list vegan foods':
            {
                axios.get('http://localhost:3001/food')
                    .then(res => {

                        let veganOnly = res.data.filter(item => item.dietary_preferences.includes('vegan'))
                        const veganIterable = {
                            index: 0,
                            [Symbol.iterator]() {
                                return this
                            },
                            next() {
                                const data = veganOnly[this.index++]
                                if (data) {
                                    return {
                                        value: data,
                                        done: false
                                    }
                                }
                                return {
                                    value: undefined,
                                    done: true
                                }
                            }
                        }

                        let data = veganIterable.next()
                        while (!data.done) {
                            console.log(data.value.name)
                            data = veganIterable.next()
                        }
                        readline.prompt()
                    })
            }
            break;
        case 'log':
            const { data } = await axios.get('http://localhost:3001/food')
            const it = data[Symbol.iterator]()
            {
                readline.question('What woud you like to log today? ', async item => {
                    let position = it.next()
                    while (!position.done) {
                        const food = position.value.name
                        if (food === item)
                            console.log(`${item} has ${position.value.calories} calories.`)
                        position = it.next()
                    }

                    readline.prompt()
                })
            }
            break;
    }
})






