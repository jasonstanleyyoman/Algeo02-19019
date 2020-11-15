<<<<<<< HEAD
import React from 'react';
import Table from '@material-ui/core/Table';

import './style.css';
  
const DataTable = ({titles, terms}) => {
    const Data = new DataTable();


    return (
        <div>{
/*            Data.Columns.Add('Term');
    
        Data.Columns.Add({titles});*/}
        </div>
    );
};

export default DataTable;

=======
import React from 'react';
import Table from '@material-ui/core/Table';

import './style.css';
  
const DataTable = ({titles, terms}) => {
    const Data = new DataTable();


    return (
        Data.Columns.Add('Term');
    
        Data.Columns.Add({titles});
    );
};

export default DataTable;

>>>>>>> 5ac8660f78f95d99ecb50dbaa5dcfcf88601936f
