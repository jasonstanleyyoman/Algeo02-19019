import React, { useEffect, useState, useStyles } from 'react';
import { GridOverlay, DataGrid } from '@material-ui/data-grid';

import './style.css';

const useData = (titles, terms) => {
    const [result, setRes] = useState({ columns: [], rows: [] });
    console.log(titles);
    console.log(titles.terms);
    console.log(titles.titles);
    
    useEffect(() => {
    const rows = [];
    var x, y, z;
    for (let i = 0; i < Object.keys(titles.terms).length; i++) {
        for (x in titles.terms) {
            console.log(x[i]);
            console.log(x)
            rows.push({cellName: x});
            console.log(Object.keys(x).length)

            for (let j = 0; j < Object.keys(x).length; j++){
                console.log(x[j])
            }
        }
    }

    const columns = [{ headerName: 'Term' }];  
    for (let i = 0; i < Object.keys(titles.titles).length; i++) {
        columns.push({ headerName: titles.titles[i] });
    }
  
    setRes({
        rows,
        columns,
      });
    }, [terms, titles]);
  
    return result;
}

function DataTable(titles, terms) {
    const result = useData(titles, terms);
    console.log(result);
    return (
        <div>
            hello
             {/*<DataGrid columns={data.columns} rows={data.rows} />*/}
        </div>
    );
};

export default DataTable;


