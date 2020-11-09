import React, {useContext, useState, useEffect} from 'react';
import ProgressBar from 'react-bootstrap/ProgressBar'
const ProgressbarContext = React.createContext();

export const useProgressbar = () => useContext(ProgressbarContext)

export const ProgressbarProvider = ({children}) => {
    const [value,setValue] = useState(0)

    useEffect(() => {
        if (value === 100) {
            setTimeout(() => {
                setValue(0)
            }, 2000)
        }
    }, [value])

    return (
        <ProgressbarContext.Provider value={{value,setValue}}>
            {
                value !== 0 ?
                <ProgressBar max={100} min={0} now={value} variant="success" animated/> :
                null
            }
            {children}
        </ProgressbarContext.Provider>
    )
}
