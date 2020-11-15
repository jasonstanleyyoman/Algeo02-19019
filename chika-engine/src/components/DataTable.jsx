import React, { useEffect, useState, useStyles } from 'react';
import { GridOverlay, DataGrid } from '@material-ui/data-grid';

import './style.css';

const useData = ({titles}, {terms}) => {
    const [data, setData] = useState({ columns: [], rows: [] });
    console.log(titles);
    
    useEffect(() => {
    const rows = [];
    for (let i = 0;i < Object.keys(titles).length; i++) {
        //rows.push({cellName: terms[i]});
    }

    const columns = [{ headerName: 'Term' }];  
    for (let i = 0; i < Object.keys(titles).length; i++) {
        columns.push({ headerName: titles[i] });
    }
  
    setData({
        rows,
        columns,
      });
    }, [terms, titles]);
  
    return data;
}

function DataTable(titles, terms) {
    const data = useData(titles, terms);
    console.log(data);
    return (
        <div>
            hello
             {/*<DataGrid columns={data.columns} rows={data.rows} />*/}
        </div>
    );
};

export default DataTable;


