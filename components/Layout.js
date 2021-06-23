const Layout = ({ children }) => {
    return (  
        <div className="container">
            <div className="site-content">
                { children }
                
            </div>
        </div>
    );
}
 
export default Layout;