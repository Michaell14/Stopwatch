import Link from "next/link"
import {useEffect} from "react"
import {useRouter} from "next/router"

const NotFound = () => {

    /*
    const router=useRouter();

    useEffecet(() => {
        setTimeout(() =>{
            router.push("https://www.youtube.com/")
        }, 300)
    }, [])
    */
    
    return (  
        <div>
            <h1>404</h1>
            <h2>This page does not exist</h2>
        </div>
    );
}
 
export default NotFound;