import { Buffer } from 'buffer';
import Link from 'next/link'; // Use this if using Next.js for client-side navigation

async function fetchLines() {
    const username = 'admin';
    const password = 'password123';
    const auth = Buffer.from(`${username}:${password}`).toString('base64');

    const res = await fetch('http://localhost:8000/json/jLines', {
        headers: {
            Authorization: `Basic ${auth}`,
        },
        cache: 'no-store',
    });

    if (!res.ok) throw new Error('Failed to fetch lines');

    const data = await res.json();
    return data.lines;
}

export default async function LinesListPage() {
    const lines = await fetchLines();

    return (
        <div>
            <h1>Available Metro Lines</h1>
            <ul style={{ listStyle: 'none', padding: 0 }}>
                {lines.map((line: any) => (
                    <li key={line.LineCode} style={{
                        padding: '1rem',
                        marginBottom: '0.5rem',
                        borderRadius: '8px',
                        borderLeft: '8px solid #333'
                    }}>
                        <Link href={`/stationsbyline/${line.LineCode}`} style={{ textDecoration: 'none', color: 'inherit' }}>
                            <strong>{line.DisplayName}</strong><br />
                            <small>
                                Start: {line.StartStationCode} | End: {line.EndStationCode}<br />
                            </small>
                        </Link>
                    </li>
                ))}
            </ul>
        </div>
    );
}
