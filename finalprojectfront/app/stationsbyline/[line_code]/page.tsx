import { Buffer } from 'buffer';

async function fetchStationsForLine(line_code: string) {
    const username = 'admin';
    const password = 'password123';
    const auth = Buffer.from(`${username}:${password}`).toString('base64');

    const res = await fetch(`http://localhost:8000/json/jStations/${line_code}`, {
        headers: {
            Authorization: `Basic ${auth}`,
        },
        cache: 'no-store',
    });

    if (!res.ok) throw new Error('Failed to fetch stations');
    const data = await res.json();
    return data.stations;
}

// Read the line_code from route params
export default async function StationListPage({ params }: { params: { line_code: string } }) {
    const lineCode = params.line_code;
    const stations = await fetchStationsForLine(lineCode);

    return (
        <div>
            <h1>Stations on the {lineCode} Line</h1>
            <ul style={{ listStyle: 'none', padding: 0 }}>
                {stations.map((station: any) => (
                    <li
                        key={station.StationCode}
                        style={{
                            backgroundColor: '#e0f7fa',
                            color: '#006064',
                            padding: '1rem',
                            marginBottom: '0.5rem',
                            borderRadius: '8px',
                        }}
                    >
                        <a
                            href={`/station/${station.StationCode}`}
                            style={{ textDecoration: 'none', color: 'inherit' }}
                        >
                            {station.Name}
                            <br />
                        </a>
                    </li>
                ))}
            </ul>
        </div>
    );
}
