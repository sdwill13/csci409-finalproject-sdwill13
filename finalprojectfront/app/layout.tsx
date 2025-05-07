import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
    variable: "--font-geist-sans",
    subsets: ["latin"],
});

const geistMono = Geist_Mono({
    variable: "--font-geist-mono",
    subsets: ["latin"],
});

export const metadata: Metadata = {
    title: "Next.js Layout App",
    description: "Learning layouts with the App Router",
};

export default function RootLayout({children}: {children: React.ReactNode})
{
    return (
        <html lang="en">
        <body>
        <header style={{padding:'1rem', backgroundColor:'#2a9a15'}}>
            <h1>CSCI*409's Final Project</h1>
            <nav>
                <a href="/">Home</a> | <a href="/lines">Lines</a>
            </nav>
        </header>
        <main style={{padding:'1rem'}}>{children}</main>
        <footer style={{padding:'1rem', backgroundColor:'#2a9a15'}}>
            <p>2025 My App</p>
        </footer>
        </body>
        </html>
    );
}
