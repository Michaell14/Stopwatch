import Footer from "../components/footer"

const Layout = ({ children }) => {
    return (  
        <div className="container">
            <div className="site-content">
                { children }
                
            </div>
            <Footer/>
        </div>
    );
}
 
export default Layout;