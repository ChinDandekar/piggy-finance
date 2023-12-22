import { Button } from 'react-bootstrap';

export function PostButton({ onButtonClick }) {
    return (
        <Button type="submit" onClick={onButtonClick}>
            Post ID Button
        </Button>
    );
}
