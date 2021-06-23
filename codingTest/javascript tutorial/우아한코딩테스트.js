function 청개구리(word){
    dict = {
        a:'z', b:'y', c:'x',d:'w',e:'v',f:'u',g:'t',h:'s',i:'r',
        j:'q',k:'p',l:'o',m:'n',n:'m',o:'l',p:'k',q:'k',s:'h',t:'g',
        u:'f',v:'e',w:'d',x:'c',y:'b',z:'a'
    }
    let wordList = [word]
    let r = [];
    for( e of wordList[0]){
        if(dict[e]){
            r.push(dict[e])
        }else if(dict[e.toLowerCase()]){
            let a = dict[e.toLowerCase()]
            r.push(a.toUpperCase())
    }else{
        r.push(' ')
    }
}  
    let resultword = ''
    r.forEach((current)=>{resultword = resultword.concat(current)});
    return resultword
}

// console.log(청개구리('I love you'))








function page(a,b){
    function innerFunc(x,y){
        if(x>y||x+1!==y||y>=400||x<=1){
        return -1}
        

        function multiply(num){
            let numbers = num.toString()
            let r = 1
            for(let i=numbers.length; i>0; i--){
                r = numbers[i-1]*r
            }
            return r
            }
    
        function add(num){
            let numbers = num.toString()
            let r = 0;
            for (let i = numbers.length; i > 0; i--) {
                r = parseInt(numbers[i - 1]) + r;
            }
            console.log(r)
            return r;
            }
    
        let higherX = Math.max(multiply(x), add(x))
        let higherY = Math.max(multiply(y), add(y))
        let higherNum = Math.max(higherX,higherY)
        return higherNum
    }

    let pobi = innerFunc(a[0],a[1])
    let crong = innerFunc(b[0],b[1])


    if(pobi==crong){
        return 0
    }
    else if(pobi>crong){
        return 1
    }
    else if(crong>pobi){
        return 2
    }

    }

// console.log('hello')
// console.log(page([97,98],[197,198]))







function count(number){
    let numberList = [];
    for(let i=number; i>0; i--){
        let current = i.toString()
        for(let i=current.length;i>0; i--){
            if(current[i-1]==3||current[i-1]==6||current[i-1]==9){
                numberList.push(current)
            }
    }}

    return numberList.length
}


console.log(count(33))






function word(word){
    let wordList = [];
    for(let i=word.length;i>0;i--){
        wordList.push(word[i-1])
    }

    function inner(wordList){
        let original = wordList
        let newList = wordList.filter((each,i,arr)=>{
            return each !== arr[i + 1] && each !== arr[i -1];
        })
        if (newList.every((e,i)=>e===original[i])){
            return newList.join('').toString()
        } else{
            return newList
        }}

    let modified = inner(wordList.reverse());
    while(typeof modified!== typeof 'h'){
        modified = inner(modified)
    }
    return modified
    
}

//console.log(word('browoanoommnaon'))






function solution(array, commands) {
    function inner(array, commands){
        let newArray = array.slice(commands[0] - 1, commands[1]).sort();
        return newArray[commands[2] - 1];
    }
    if(typeof commands[0] == typeof[]){
        let answer = commands.map((e)=>inner(array,e));
        return answer
    } else{
        let answer2 = inner(array,commands);
        return answer2
    }
    }
    
    
console.log(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]));

console.log(solution([1, 5, 2, 6, 3, 7, 4],[4, 4, 1]))
console.log(solution([1, 5, 2, 6, 3, 7, 4],[2,5,3]))
console.log(solution([1, 5, 2, 6, 3, 7, 4], [1,7,3]))