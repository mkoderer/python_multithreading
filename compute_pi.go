package main
import (
    "fmt"
    "sync"
    "os"
    "strconv"
)

var wg sync.WaitGroup

func calc_pi(){
    defer wg.Done()
    var k float64 = 1
    var s float64 = 0

    for i := 0; i < 10000000000; i++ {
        if i % 2 == 0{
            s = s + 4/k
        } else {
            s = s - 4/k
        }
        k += 2
    }
    fmt.Println(s)

}

func main() {
    num_threads, err := strconv.Atoi(os.Args[1])
    if err != nil {
        fmt.Println("Wrong argument")
        return
    }

    wg.Add(num_threads)
    for t := 0; t < int(num_threads); t++{
        fmt.Println("Adding gofunc")
        go calc_pi()    
    }
    wg.Wait()
    
}