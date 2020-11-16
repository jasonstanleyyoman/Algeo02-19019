import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import './style.css';

const useStyles = makeStyles({
  table: {
    minWidth: 650,
  },
});

const useData = (titles, terms) => {
    var columns = []
    var rows = []




    const termKeys = Object.keys(terms)
    for (let i = 0;i < termKeys.length; i++) {
        const row = {}
        row.cellName = termKeys[i]
        row.row = terms[termKeys[i]]

        rows.push(row);
    }
    console.log("rows", rows)

    columns = [{ headerName: 'Term' }];
    for (let i = 0; i < titles.length; i++) {
        columns.push({ headerName: titles[i] });
    }
    console.log("columns", columns)


    return [columns,rows];
}

function DataTable({titles, terms}) {
    const [columns, rows] = useData(titles, terms);
    const classes = useStyles();
    // console.log(data);
    return (
        <div>

             <TableContainer component={Paper}>
                 <Table className={classes.table}>
                     <TableHead>
                         <TableRow>
                             {columns.map(col =>
                                 <TableCell component="th" scope="row">
                                     {col.headerName}
                                 </TableCell>)}
                         </TableRow>
                     </TableHead>
                     <TableBody>

                             {rows.map(row => {
                                 let dataRow = row.row.map(r => <TableCell component="th" scope="row">{r}</TableCell>)
                                 let component = (
                                     <TableRow>
                                         <TableCell component="th" scope="row">{row.cellName}</TableCell>
                                         {dataRow}
                                     </TableRow>

                                 )

                                 return component
                             })}

                     </TableBody>
                 </Table>
             </TableContainer>
        </div>
    );
};

export default DataTable;
