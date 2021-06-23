import Navbar from "../components/navbar"
import Footer from "../components/footer"

const Layout = ({ children }) => {
    return (  
        <div className="container">
            <div className="site-content">
                <Navbar/>
                { children }
                
            </div>
            <Footer/>
        </div>
    );
}
 
export default Layout;