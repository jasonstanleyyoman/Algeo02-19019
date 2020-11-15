<<<<<<< HEAD
import React from 'react';
import './style.css';

const Feed = ({links, similarity, title, sentence, total_words}) => {
    
    return (
        <div class='feed'>
            <h2 class='feed-title'><a href={links}target="_blank">{title}</a></h2>
            <div class='feed-text'><p>{sentence}</p></div>
            <div class='row'>
                <div class='col-3'>
                    <div class='row feed-subtext-title'>Total Words</div>
                    <div class='row feed-subtext-info'>{total_words}</div>
                </div>
                <div class='col-3'>
                    <div class='row feed-subtext-title'>Similarity</div>
                    <div class='row feed-subtext-info'>{similarity}%</div>
                </div>
                <div class='col'></div>
            </div>
                
        </div>
    );
};

=======
import React from 'react';
import './style.css';

const Feed = ({links, similarity, title, sentence, total_words}) => {
    
    return (
        <div class='feed'>
            <h2 class='feed-title'><a href={links}target="_blank">{title}</a></h2>
            <div class='feed-text'><p>{sentence}</p></div>
            <div class='row'>
                <div class='col-3'>
                    <div class='row feed-subtext-title'>Total Words</div>
                    <div class='row feed-subtext-info'>{total_words}</div>
                </div>
                <div class='col-3'>
                    <div class='row feed-subtext-title'>Similarity</div>
                    <div class='row feed-subtext-info'>{similarity}%</div>
                </div>
                <div class='col'></div>
            </div>
                
        </div>
    );
};

>>>>>>> 5ac8660f78f95d99ecb50dbaa5dcfcf88601936f
export default Feed;