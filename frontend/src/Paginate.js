import { Link } from "react-router-dom";
import Sidebar from './Sidebar';
import useFetch from './useFetch';


const Paginate = ( blogs, url ) => {

  const handlePageNumber = ( page, active, url ) => {
    if ( page ) {
      if ( active ) {
        return (
        <a class='active'>{ page }</a>
      )} else {
        return (
         <Link to={ `${ url }/page/${ page }` }>{ page }</Link>
      )}
  }}

  const handlePreviousNext = ( page, title, url ) => {
    if ( page ) {
      return (
        <Link to={ `${ url }/page/${ page }` }>{ title }</Link>
      )} else {
        return (
          <a class='active'>Previous</a>
  )}}

  const handlePaginator = ( blog_objects ) => {
    if ( blog_objects.total_pages > 1) {
      return (
        <div>
          { handlePreviousNext(blogs.previous_page_number, 'Previous', url) }
          { handlePageNumber(blogs.previous_page_number, null, url) }
          { handlePageNumber(blogs.current_page_number, true, url) }
          { handlePageNumber(blogs.next_page_number, null, url) }
          { handlePreviousNext(blogs.next_page_number, 'Next', url) }
        </div>
      )}}

  return (
    <div className="pagination">
      { handlePaginator( blogs ) }
    </div>
  );
}

export default Paginate;

